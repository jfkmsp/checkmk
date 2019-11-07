MK_LIVESTATUS := mk-livestatus
MK_LIVESTATUS_VERS := $(CMK_VERSION)
MK_LIVESTATUS_DIR := $(MK_LIVESTATUS)-$(MK_LIVESTATUS_VERS)

# Attention: copy-n-paste from check_mk/Makefile below...
MK_LIVESTATUS_BUILD := $(BUILD_HELPER_DIR)/$(MK_LIVESTATUS_DIR)-build
MK_LIVESTATUS_UNPACK := $(BUILD_HELPER_DIR)/$(MK_LIVESTATUS_DIR)-unpack
MK_LIVESTATUS_INSTALL := $(BUILD_HELPER_DIR)/$(MK_LIVESTATUS_DIR)-install

.PHONY: $(MK_LIVESTATUS) $(MK_LIVESTATUS)-build $(MK_LIVESTATUS)-install $(MK_LIVESTATUS)-skel $(MK_LIVESTATUS)-clean

$(MK_LIVESTATUS): $(MK_LIVESTATUS_BUILD)
$(MK_LIVESTATUS)-install: $(MK_LIVESTATUS_INSTALL)
$(MK_LIVESTATUS)-build: $(MK_LIVESTATUS_BUILD)

$(PACKAGE_DIR)/$(MK_LIVESTATUS)/$(MK_LIVESTATUS_DIR).tar.gz:
	$(MAKE) -C $(REPO_PATH) omd/packages/mk-livestatus/$(MK_LIVESTATUS_DIR).tar.gz

# TODO: Why can't we use $(RRDTOOL_BUILD_LIBRARY) as dependency here?
$(MK_LIVESTATUS_BUILD): $(MK_LIVESTATUS_UNPACK) $(BOOST_BUILD) $(RE2_BUILD) $(RRDTOOL)-build-library
# TODO: Improve the rrdtool hacks below
	cd $(MK_LIVESTATUS_DIR) ; \
	    export CPPFLAGS=-I$(REPO_PATH)/omd/$(RRDTOOL_DIR)/src ; \
	    export LDFLAGS=-L$(REPO_PATH)/omd/$(RRDTOOL_DIR)/src/.libs ; \
	    ./configure CXXFLAGS="-g -O3 -Wall -Wextra" --with-boost=$(PACKAGE_BOOST_DESTDIR) --with-re2=$(PACKAGE_RE2_DESTDIR) --prefix=$(OMD_ROOT) && \
	    $(MAKE) all
	$(TOUCH) $@

$(MK_LIVESTATUS_INSTALL): $(MK_LIVESTATUS_BUILD)
	$(MAKE) -j1 DESTDIR=$(DESTDIR) -C $(MK_LIVESTATUS_DIR) install
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/bin
	install -m 755 $(PACKAGE_DIR)/$(MK_LIVESTATUS)/lq $(DESTDIR)$(OMD_ROOT)/bin
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/lib/python
	install -m 644 $(MK_LIVESTATUS_DIR)/api/python/livestatus.py $(DESTDIR)$(OMD_ROOT)/lib/python
	install -m 755 $(PACKAGE_DIR)/$(MK_LIVESTATUS)/LIVESTATUS_TCP $(DESTDIR)$(OMD_ROOT)/lib/omd/hooks/
	install -m 755 $(PACKAGE_DIR)/$(MK_LIVESTATUS)/LIVESTATUS_TCP_ONLY_FROM $(DESTDIR)$(OMD_ROOT)/lib/omd/hooks/
	install -m 755 $(PACKAGE_DIR)/$(MK_LIVESTATUS)/LIVESTATUS_TCP_PORT $(DESTDIR)$(OMD_ROOT)/lib/omd/hooks/
	install -m 755 $(PACKAGE_DIR)/$(MK_LIVESTATUS)/LIVESTATUS_TCP_TLS $(DESTDIR)$(OMD_ROOT)/lib/omd/hooks/
	$(TOUCH) $@

$(MK_LIVESTATUS)-skel:

$(MK_LIVESTATUS)-clean:
	$(RM) -r mk-livestatus-*.*.*[0-9] $(BUILD_HELPER_DIR)/$(MK_LIVESTATUS)*
