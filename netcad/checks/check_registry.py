from netcad.registry import Registry
from .check_collection import CheckCollection

__all__ = ["CheckRegistry", "register_collection"]


class CheckRegistry(Registry, registry_name="test_services"):
    """
    TestingServices registry used to register TestCases class so that they can
    be looked up by name for the purposes of building tests, ...
    """

    def __call__(self, cls):
        """
        The __call__ method is used a decorator.  For example:

            @testing_services
            class FooTestCases(TestCases):
                name = 'foo-service'
                ...

        The __call__ decorator will validate that the decorating class is of
        type TestCases and has a "services" attribute defined.

        Parameters
        ----------
        cls: type
            The TestCases subclass to register with TestingServices.

        Returns
        -------
        cls - as is
        """

        if not issubclass(cls, CheckCollection):
            raise RuntimeError(
                f"Forbidden use of TestingService registration on non {CheckCollection.__name__} class: {cls.__name__}"
            )

        try:
            name = cls.get_name()
        except (KeyError, AttributeError):
            raise RuntimeError(
                f"TestCases: {cls.__name__}: missing `name` name attribute."
            )

        self.registry_add(name, cls)
        return cls


# decorator function is the registration, see __call__ usage above.
register_collection = CheckRegistry()