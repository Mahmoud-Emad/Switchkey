from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from switchkeys.services.organizations import get_organization_by_id
from switchkeys.models.management import Organization
from switchkeys.api.permissions import UserIsAuthenticated, IsAdminUser
from switchkeys.serializers.projects import OrganizationProjectSerializer
from switchkeys.services.projects import get_all_projects, get_project_by_id
from switchkeys.api.custom_response import CustomResponse


class BaseOrganizationProjectApiView(ListAPIView):
    serializer_class = OrganizationProjectSerializer
    permission_classes = []

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                UserIsAuthenticated,
            ]
        else:
            self.permission_classes = [
                IsAdminUser,
            ]

        return super(BaseOrganizationProjectApiView, self).get_permissions()

    def get_queryset(self) -> Response:
        """Get all ``projects`` in the system."""
        get_queryset = get_all_projects()
        return get_queryset

    def post(self, request: Request) -> Response:
        """Create new organization project."""

        project = request.data
        serializer = self.get_serializer(data=project)
        if serializer.is_valid():
            organization_id: int = serializer.validated_data.get("organization_id")
            organization = get_organization_by_id(str(organization_id))

            if organization is None:
                return CustomResponse.not_found(
                    message="Organization not found."
                )

            if request.user.id != organization.owner.id:
                return CustomResponse.unauthorized(
                    message="You do not have permission to access this resource because you are not the creator of this organization.",
                )

            serializer.save(organization=organization)

            return CustomResponse.success(
                data=serializer.data,
                message="Organization project has been created successfully.",
            )

        return CustomResponse.bad_request(
            message="Please make sure that you entered a valid data.",
            error=serializer.errors,
            data=request.data,
        )


class OrganizationProjectApiView(GenericAPIView):
    serializer_class = OrganizationProjectSerializer
    permission_classes = []

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = []
        else:
            self.permission_classes = [
                IsAdminUser,
            ]

        return super(OrganizationProjectApiView, self).get_permissions()

    def get(self, request: Request, project_id: str) -> Response:
        """Get an organization project by its ID."""
        project = get_project_by_id(project_id)

        if project is None:
            return CustomResponse.not_found(
                message="The organization project does not exist."
            )
        return CustomResponse.success(
            data=OrganizationProjectSerializer(project).data,
            message="The organization project found.",
        )

    def put(self, request: Request, project_id: str) -> Response:
        """Update an organization project by its ID."""
        project = get_project_by_id(project_id)

        if project is None:
            return CustomResponse.not_found(
                message="The organization project does not exist."
            )

        data = request.data
        serializer = self.get_serializer(project, data=data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse.success(
                data=serializer.data,
                message="Organization project has been updated successfully.",
                status_code=201,
            )

        return CustomResponse.bad_request(
            data=OrganizationProjectSerializer(project).data,
            message="Please make sure that you entered a valid data..",
            error=serializer.errors,
        )

    def delete(self, request: Request, project_id: str) -> Response:
        """Delete an organization project by its ID."""
        project = get_project_by_id(project_id)

        if project is None:
            return CustomResponse.not_found(
                message="The organization project does not exist."
            )

        project.delete()
        return CustomResponse.success(
            data={},
            message="Organization project has been updated successfully.",
            status_code=204,
        )