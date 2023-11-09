from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    관리자에게 읽기/쓰기/나만 보기/삭제 권한을 부여하고 다른 사용자에게는 읽기/쓰기 권한을 부여하는 권한 클래스
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_staff:  # 관리자인 경우
                return True  # 모든 권한 부여
            return request.method in permissions.SAFE_METHODS  # 다른 사용자에게는 읽기/쓰기 권한 부여
        return False  # 로그인하지 않은 사용자에게는 권한 없음
