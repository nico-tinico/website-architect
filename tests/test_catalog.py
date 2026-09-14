from structio.catalog.profiles import PROFILES
from structio.domain.enums import SiteType, Topology


def test_all_site_types_have_profiles() -> None:
    assert set(PROFILES) == set(SiteType)


def test_topology_defaults() -> None:
    assert PROFILES[SiteType.LANDING_PAGE].default_topology is Topology.SEQUENTIAL
    assert PROFILES[SiteType.SAAS].default_topology is Topology.HIERARCHICAL
    assert PROFILES[SiteType.ECOMMERCE].default_topology is Topology.MATRIX