# -*- encoding: utf-8
# yapf: disable
checkname = u'postfix_mailq'

info = [
    [u'[[[]]]'], [u'QUEUE_deferred', u'2', u'1'],
    [u'QUEUE_active', u'4', u'3'], [u'[[[/etc/postfix-internal]]]'],
    [u'QUEUE_deferred', u'2', u'1'], [u'QUEUE_active', u'4', u'3']
]

discovery = {'': [(u'', {}), (u'/etc/postfix-internal', {})]}

checks = {
    '': [
        (
            u'', {
                'active': (200, 300),
                'deferred': (10, 20)
            }, [
                (
                    0, u'Deferred queue length: 1', [
                        ('length', 1, 10, 20, None, None),
                        ('size', 2, None, None, None, None)
                    ]
                ),
                (
                    0, u'Active queue length: 3', [
                        ('mail_queue_active_length', 3, 200, 300, None, None),
                        ('mail_queue_active_size', 4, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            u'/etc/postfix-internal', {
                'active': (200, 300),
                'deferred': (10, 20)
            }, [
                (
                    0, u'Deferred queue length: 1', [
                        ('length', 1, 10, 20, None, None),
                        ('size', 2, None, None, None, None)
                    ]
                ),
                (
                    0, u'Active queue length: 3', [
                        ('mail_queue_active_length', 3, 200, 300, None, None),
                        ('mail_queue_active_size', 4, None, None, None, None)
                    ]
                )
            ]
        )
    ]
}
