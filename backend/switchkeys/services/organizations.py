from typing import List
from switchkeys.models.users import User
from switchkeys.models.management import Organization, OrganizationProject


def get_all_organization() -> List[Organization]:
    """Return all organization"""
    return Organization.objects.all().order_by("name")


def get_organization_by_id(id: str) -> Organization:
    """Return organization who has the same id"""
    if not id.isdigit():
        return None
    try:
        return Organization.objects.get(id=int(id))
    except Organization.DoesNotExist:
        return None


def check_organization_name(user: User, name: str):
    """Check if there is an organization created by the requested user with the same name"""
    organizations = Organization.objects.filter(name=name, owner__id=user.id)
    return len(organizations) > 0


def get_user_organization_by_name(user: User, name: str):
    """Get the organization based on the user and the organization name"""
    try:
        organization = Organization.objects.get(
            owner__id=user.id,
            name=name,
        )
        return organization
    except Organization.DoesNotExist:
        return None


def get_organization_projects(organization_id: str) -> List[OrganizationProject]:
    """Filter all projects and get only the projects that has the same organization ID."""
    return OrganizationProject.objects.filter(organization__id=organization_id)


def filter_organization_by_owner(user: User) -> List[Organization]:
    """
    Filter organizations by owner user

    ### Attributes
        - user (User): The user object to filter the organizations based on the user.

    ### Returns
        - a list of organizations as queryset.
    """

    return Organization.objects.filter(owner__id=user.id)
