#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import shutil
from pathlib import Path
from typing import Final, Generator

import pytest

from tests.testlib.site import Site

import cmk.utils.msi_engine as msi_engine
import cmk.utils.obfuscate as obfuscate

MSI_LOCATION: Final = "share/check_mk/agents/windows"
EXPECTED_EXECUTABLES: Final = ["msiinfo", "msibuild", "lcab"]
EXPECTED_TEST_FILES: Final = ["check_mk_agent.msi", msi_engine.AGENT_MSI_FILE, "check_mk.user.yml"]
TEST_MSI_FILE: Final = Path("agents/wnx/test_files/msibuild/msi") / "check_mk_agent.msi"


@pytest.mark.parametrize("executable", EXPECTED_EXECUTABLES)
def test_executables(site: Site, executable) -> None:  # type:ignore[no-untyped-def]
    p = Path(site.path("bin")) / executable
    assert p.exists(), f"path: '{p}' exe: '{executable}'"


@pytest.mark.parametrize("test_file", EXPECTED_TEST_FILES)
def test_files(site: Site, test_file) -> None:  # type:ignore[no-untyped-def]
    p = Path(site.path(MSI_LOCATION)) / test_file
    assert p.exists(), f"path: '{p}' file: '{test_file}'"


def _get_msi_file_path_not_signed(site: Site) -> Path:
    return Path(site.path(MSI_LOCATION)) / msi_engine.AGENT_MSI_FILE


@pytest.fixture(name="out_dir")
def fixture_out_dir(tmp_path: Path) -> Generator[Path, None, None]:
    out_dir = tmp_path / "idts"
    out_dir.mkdir()
    yield out_dir
    if out_dir.exists():
        shutil.rmtree(str(out_dir))


def _create_msi_file(site: Site, *, out_dir: Path) -> Path:
    msi_file: Final = _get_msi_file_path_not_signed(site)
    out_file = out_dir / "deobfuscated.msi"
    obfuscate.deobfuscate_file(msi_file, file_out=out_file)
    return out_file


# check the export with site/bin tools
def test_export_msi_file_table(site: Site, out_dir: Path) -> None:
    msi_file = _create_msi_file(site, out_dir=out_dir)
    for name in ["File", "Property", "Component"]:
        msi_engine._export_msi_file_table(
            Path(site.path("bin/")),
            name=name,
            msi_in=msi_file,
            out_dir=out_dir,
        )
        f = out_dir / (name + ".idt")
        assert f.stat().st_size > 0, f"Ups for [{name}] in {f}"


@pytest.fixture(name="pos_initial", scope="module")
def fixture_pos_initial() -> int:
    return TEST_MSI_FILE.read_bytes().find(b"4E18343A-5E32-1")


@pytest.fixture(name="work_file")
def fixture_work_file(tmp_path: Path) -> Path:
    tgt: Final = tmp_path / "check_mk_agent.msi"
    shutil.copy(TEST_MSI_FILE, dst=tgt)
    return tgt


def test_update_package_code_random_uuid(work_file: Path) -> None:
    msi_engine.update_package_code(work_file, package_code=None)
    assert work_file.read_bytes().find(b"4E18343A-5E32-1") == -1


def test_update_package_code_fixed_uuid(pos_initial: int, work_file: Path) -> None:
    msi_engine.update_package_code(work_file, package_code="{01234567-1234-1234-1234-012345678901}")
    assert work_file.read_bytes().find(b"01234567-1234-1234") == pos_initial


def test_update_package_code_hash(pos_initial: int, work_file: Path) -> None:
    msi_engine.update_package_code(work_file, package_code="012")
    assert work_file.read_bytes().find(b"21FAC8EF-8042-50CA-8C85-FBCA566E726E") == pos_initial


def test_copy_or_create(tmp_path: Path) -> None:
    src_file = tmp_path / "temp.x.in"
    dst_file = tmp_path / "temp.x.out"

    # src file doesn't exist, check file created
    msi_engine.copy_or_create(src_file, dst_file=dst_file, text="!!!")
    assert dst_file.read_text() == "!!!"

    # src files exists check file copied
    src_file.write_text("+++")
    msi_engine.copy_or_create(src_file, dst_file=dst_file, text="!!!")
    assert dst_file.read_text() == "+++"
