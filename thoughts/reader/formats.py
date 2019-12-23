class fmt:

    ID_NAME_LENGTH_FORMAT = '<QI'
    BYTE_ARRAY_FORMAT = lambda length: '<{0}s'.format(length)

    BIRTH_GENDER_FORMAT = 'Ic'

    TIME_FORMAT = 'Q'

    TRNSL_FORMAT = 'ddd'

    ROTATE_IMWIDTH_IMHIGHT_FORMAT = 'ddddII'

    DEPTH_IMWIDTH_IMHIGHT_FORMAT = 'II'

    FEELING_FORMAT = 'ffff'