from modules.security.security import SecuritySystem
from core.singleton.logger import Logger

class SecurityProxy:
    def __init__(self, user_role='guest'):
        self._real = SecuritySystem()
        self.role = user_role
        self.logger = Logger.get_instance()

    def get_status(self):
        if self.role in ('admin', 'operator'):
            self.logger.log(f'Authorized status check by {self.role}')
            print(self._real.status())
        else:
            self.logger.log(f'Unauthorized status check attempt by {self.role}')
            print('Access denied: insufficient privileges')

    def arm(self):
        if self.role == 'admin':
            self._real.arm()
            print('Security armed')
        else:
            print('Only admin can arm the system')
