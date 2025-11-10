def admin_access():
    return "Access granted: Full"

def editor_access():
    return "Access granted: Partial"

def viewer_access():
    return "Access granted: Read-only"

def default_access():
    return "Access denied"
access_map = {
    "admin": admin_access,
    "editor": editor_access,
    "viewer": viewer_access
}
def default_access():
    return

def main():
  user_role='admin'
  result = access_map.get(user_role, default_access)()
  print(result)
if __name__ == "__main__":
  main()
