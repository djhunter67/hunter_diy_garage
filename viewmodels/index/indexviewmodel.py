from viewmodels.shared.viewmodel_base import ViewModelBase
from starlette.requests import Request

class IndexViewModel(ViewModelBase):
    
    def __init__(self, request: Request) -> None:
        super().__init__(request)

        self.user_name: str = "Christerpher"

class AccountViewModel(ViewModelBase):

    def __init__(self, request: Request) -> None:
        super().__init__(request)

        self.account = "templates/account/account.pt"
        