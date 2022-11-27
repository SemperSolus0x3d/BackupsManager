import inject
from impl import MountService, TopLevelExceptionHandler

if __name__ == '__main__':
    with inject.instance(TopLevelExceptionHandler).handleExceptions():
        inject.instance(MountService).mountUsbRepo()
