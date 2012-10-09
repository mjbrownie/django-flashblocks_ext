__doc__ = """
Additional Flatblock 'permission_check' functions
"""

def group_slug_permisson_check(request,flatblock):
    """
    A flatblock slug must be of the form 'groupname.flatblock_name' for success
    """

    if request.user.is_superuser:
        return True

    try:
        group, slug = flatblock.slug.split('.')
    except:
        #most likely a different slug name convention
        return False

    if request.user.groups.filter(name=group).count() == 1:
        return True

    return False
