from bot.multithreading.worker import Worker

from clock.storage.async.operation import StorageOperation


class StorageScheduler:
    def __init__(self, worker: Worker):
        self.worker = worker
        self.context_manager = None

    def set_context_manager(self, context_manager):
        self.context_manager = context_manager

    def schedule_no_result(self, func: callable):
        return self._schedule(func, ignore_result=True)

    def schedule_with_result(self, func: callable):
        return self._schedule(func, ignore_result=False)

    def _schedule(self, func: callable, ignore_result: bool):
        return StorageOperation(self.worker, self.context_manager, func, ignore_result).execute()
