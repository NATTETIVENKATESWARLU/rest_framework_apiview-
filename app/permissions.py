from rest_framework.permissions import BasePermission,SAFE_METHODS

class is_readonly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False
        


class is_GetPatch(BasePermission):
    def has_permission(self, request, view):
        allowed_methods = ["GET", "PATCH","PUT"]
        if request.method in allowed_methods:
            return True
        else:
            return False
        

class is_User(BasePermission):
    def has_permission(self, request, view):
        users=request.user.username
        

        if users.lower()=="venkat":
            return True
        elif users!="" and len(users)%2==0 and request.method in SAFE_METHODS:
            return True
        else:
            return False
        