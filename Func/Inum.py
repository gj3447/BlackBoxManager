from enum import Enum

#main_window 상태들
class State(Enum):
    DEFAULT = 1
    CAMERA_RUN = 2
    EDIT_CUT = 3
    EDIT_CUT_DRAG = 4
    EDIT_SIZE = 5
    