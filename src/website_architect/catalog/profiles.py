from website_architect.domain.enums import LinkType, NodeType, SiteType, Topology
from website_architect.domain.nodes import PageDefinition

from .definitions import LinkRule, SiteProfile, profile


# ---------------------------------------------------------------------------
# Definition helpers
# ---------------------------------------------------------------------------


def section(
    name: str,
    *,
    required: bool = True,
    purpose: str | None = None,
) -> PageDefinition:
    return PageDefinition(
        name=name,
        node_type=NodeType.SECTION,
        required=required,
        repeatable=False,
        purpose=purpose,
        children=(),
    )


def page(
    name: str,
    *,
    required: bool = True,
    repeatable: bool = False,
    purpose: str | None = None,
    children: tuple[PageDefinition, ...] = (),
) -> PageDefinition:
    return PageDefinition(
        name=name,
        node_type=NodeType.PAGE,
        required=required,
        repeatable=repeatable,
        purpose=purpose,
        children=children,
    )


def template(
    name: str,
    *,
    required: bool = True,
    purpose: str | None = None,
    children: tuple[PageDefinition, ...] = (),
) -> PageDefinition:
    return PageDefinition(
        name=name,
        node_type=NodeType.TEMPLATE,
        required=required,
        repeatable=True,
        purpose=purpose,
        children=children,
    )


def collection(
    name: str,
    *,
    required: bool = True,
    purpose: str | None = None,
    children: tuple[PageDefinition, ...] = (),
) -> PageDefinition:
    return PageDefinition(
        name=name,
        node_type=NodeType.COLLECTION,
        required=required,
        repeatable=False,
        purpose=purpose,
        children=children,
    )


# ---------------------------------------------------------------------------
# Landing Page
# ---------------------------------------------------------------------------


LANDING_PAGE = profile(
    site_type=SiteType.LANDING_PAGE,
    topology=Topology.SEQUENTIAL,
    single_page=(
        section("Hero"),
        section("Value Proposition"),
        section("Problem", required=False),
        section("Solution"),
        section("Features", required=False),
        section("Benefits", required=False),
        section("Social Proof", required=False),
        section("Testimonials", required=False),
        section("Pricing", required=False),
        section("FAQ", required=False),
        section("CTA"),
    ),
    multi_page=(
        page("Product", required=False),
        page("Features", required=False),
        page("Pricing", required=False),
        page("About", required=False),
        page("FAQ", required=False),
        page("Contact", required=False),
    ),
    single_page_links=(
        LinkRule("Hero", "Value Proposition", LinkType.NAVIGATION),
        LinkRule("Value Proposition", "Solution", LinkType.NAVIGATION),
        LinkRule("Solution", "Features", LinkType.NAVIGATION),
        LinkRule("Features", "Social Proof", LinkType.NAVIGATION),
        LinkRule("Social Proof", "Pricing", LinkType.NAVIGATION),
        LinkRule("Pricing", "FAQ", LinkType.NAVIGATION),
        LinkRule("FAQ", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
        LinkRule("Pricing", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Product", LinkType.NAVIGATION),
        LinkRule("Home", "Features", LinkType.NAVIGATION),
        LinkRule("Home", "Pricing", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Product", "Contact", LinkType.CTA),
        LinkRule("Pricing", "Contact", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# SaaS
# ---------------------------------------------------------------------------


SAAS = profile(
    site_type=SiteType.SAAS,
    topology=Topology.HIERARCHICAL,
    single_page=(
        section("Hero"),
        section("Product Overview"),
        section("Features"),
        section("Integrations", required=False),
        section("Security", required=False),
        section("Use Cases", required=False),
        section("Testimonials", required=False),
        section("Pricing"),
        section("FAQ", required=False),
        section("CTA"),
    ),
    multi_page=(
        page(
            "Product",
            children=(
                page("Overview"),
                page("Features"),
                page("Integrations", required=False),
                page("Security", required=False),
            ),
        ),
        page(
            "Solutions",
            required=False,
            children=(
                page("Startups"),
                page("Teams"),
                page("Enterprise"),
            ),
        ),
        page("Pricing"),
        page(
            "Resources",
            required=False,
            children=(
                page("Blog"),
                page("Documentation"),
                page("Guides"),
                page("Changelog"),
            ),
        ),
        page(
            "Company",
            required=False,
            children=(
                page("About"),
                page("Careers"),
                page("Contact"),
            ),
        ),
        page("Login"),
        page("Signup"),
    ),
    single_page_links=(
        LinkRule("Hero", "Product Overview", LinkType.NAVIGATION),
        LinkRule("Product Overview", "Features", LinkType.NAVIGATION),
        LinkRule("Features", "Integrations", LinkType.NAVIGATION),
        LinkRule("Features", "Security", LinkType.NAVIGATION),
        LinkRule("Security", "Pricing", LinkType.NAVIGATION),
        LinkRule("Pricing", "FAQ", LinkType.NAVIGATION),
        LinkRule("FAQ", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
        LinkRule("Pricing", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Product", LinkType.NAVIGATION),
        LinkRule("Home", "Solutions", LinkType.NAVIGATION),
        LinkRule("Home", "Pricing", LinkType.NAVIGATION),
        LinkRule("Home", "Resources", LinkType.NAVIGATION),
        LinkRule("Home", "Company", LinkType.NAVIGATION),
        LinkRule("Home", "Login", LinkType.NAVIGATION),
        LinkRule("Product", "Signup", LinkType.CTA),
        LinkRule("Pricing", "Signup", LinkType.CTA),
        LinkRule("Solutions", "Signup", LinkType.CTA),
        LinkRule(
            "Company",
            "Company.Contact",
            LinkType.NAVIGATION,
        ),
    ),
)


# ---------------------------------------------------------------------------
# Agency
# ---------------------------------------------------------------------------


AGENCY = profile(
    site_type=SiteType.AGENCY,
    topology=Topology.HIERARCHICAL,
    single_page=(
        section("Hero"),
        section("Services"),
        section("Work"),
        section("About"),
        section("Process", required=False),
        section("Clients", required=False),
        section("Testimonials", required=False),
        section("Team", required=False),
        section("FAQ", required=False),
        section("Contact"),
    ),
    multi_page=(
        page(
            "Services",
            children=(
                template("Service"),
            ),
        ),
        page(
            "Work",
            children=(
                template("Case Study"),
            ),
        ),
        page(
            "About",
            children=(
                page("Team", required=False),
                page("Process", required=False),
                page("Values", required=False),
            ),
        ),
        page(
            "Insights",
            required=False,
            children=(
                page("Blog", required=False),
                page("Articles", required=False),
            ),
        ),
        page("Contact"),
    ),
    single_page_links=(
        LinkRule("Hero", "Services", LinkType.NAVIGATION),
        LinkRule("Services", "Work", LinkType.NAVIGATION),
        LinkRule("Work", "About", LinkType.NAVIGATION),
        LinkRule("About", "Testimonials", LinkType.NAVIGATION),
        LinkRule("Testimonials", "Contact", LinkType.NAVIGATION),
        LinkRule("Hero", "Contact", LinkType.CTA),
        LinkRule("Work", "Contact", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Services", LinkType.NAVIGATION),
        LinkRule("Home", "Work", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Insights", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Services", "Contact", LinkType.CTA),
        LinkRule("Work", "Contact", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# Portfolio
# ---------------------------------------------------------------------------


PORTFOLIO = profile(
    site_type=SiteType.PORTFOLIO,
    topology=Topology.SEQUENTIAL,
    single_page=(
        section("Hero"),
        section("About"),
        section("Selected Work"),
        section("Skills", required=False),
        section("Experience", required=False),
        section("Testimonials", required=False),
        section("Contact"),
    ),
    multi_page=(
        page(
            "Work",
            children=(
                template("Project"),
            ),
        ),
        page("About"),
        page("Experience", required=False),
        page("Skills", required=False),
        page("Journal", required=False),
        page("Contact"),
    ),
    single_page_links=(
        LinkRule("Hero", "About", LinkType.NAVIGATION),
        LinkRule("About", "Selected Work", LinkType.NAVIGATION),
        LinkRule("Selected Work", "Skills", LinkType.NAVIGATION),
        LinkRule("Skills", "Experience", LinkType.NAVIGATION),
        LinkRule("Experience", "Testimonials", LinkType.NAVIGATION),
        LinkRule("Testimonials", "Contact", LinkType.NAVIGATION),
        LinkRule("Hero", "Selected Work", LinkType.CTA),
        LinkRule("Selected Work", "Contact", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Work", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Experience", LinkType.NAVIGATION),
        LinkRule("Home", "Skills", LinkType.NAVIGATION),
        LinkRule("Home", "Journal", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Work", "Contact", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# Ecommerce
# ---------------------------------------------------------------------------


ECOMMERCE = profile(
    site_type=SiteType.ECOMMERCE,
    topology=Topology.MATRIX,
    single_page=(
        section("Hero"),
        section("Featured Products"),
        section("Categories"),
        section("Collections", required=False),
        section("Best Sellers", required=False),
        section("New Arrivals", required=False),
        section("Offers", required=False),
        section("Reviews", required=False),
        section("CTA"),
    ),
    multi_page=(
        page(
            "Shop",
            children=(
                collection(
                    "Category",
                    children=(
                        template("Product"),
                    ),
                ),
                collection(
                    "Collections",
                    required=False,
                    children=(
                        template("Collection"),
                    ),
                ),
                page("Search", required=False),
            ),
        ),
        template("Product"),
        page("Wishlist", required=False),
        page("Cart"),
        page("Checkout"),
        page(
            "Account",
            required=False,
            children=(
                page("Profile"),
                page("Orders"),
                page("Addresses"),
            ),
        ),
        page("Journal", required=False),
        page("Support", required=False),
    ),
    single_page_links=(
        LinkRule("Hero", "Featured Products", LinkType.NAVIGATION),
        LinkRule("Featured Products", "Categories", LinkType.NAVIGATION),
        LinkRule("Categories", "Collections", LinkType.NAVIGATION),
        LinkRule("Collections", "Best Sellers", LinkType.NAVIGATION),
        LinkRule("Best Sellers", "New Arrivals", LinkType.NAVIGATION),
        LinkRule("New Arrivals", "Offers", LinkType.NAVIGATION),
        LinkRule("Offers", "Reviews", LinkType.NAVIGATION),
        LinkRule("Reviews", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Shop", LinkType.NAVIGATION),
        LinkRule("Home", "Wishlist", LinkType.NAVIGATION),
        LinkRule("Home", "Cart", LinkType.NAVIGATION),
        LinkRule("Home", "Account", LinkType.NAVIGATION),
        LinkRule("Home", "Journal", LinkType.NAVIGATION),
        LinkRule("Shop", "Shop.Category.Product", LinkType.NAVIGATION),
        LinkRule("Shop.Category.Product", "Wishlist", LinkType.CTA),
        LinkRule("Shop.Category.Product", "Cart", LinkType.CTA),
        LinkRule("Cart", "Checkout", LinkType.NAVIGATION),
        LinkRule("Checkout", "Account", LinkType.NAVIGATION),
        LinkRule("Journal", "Shop", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# Travel
# ---------------------------------------------------------------------------


TRAVEL = profile(
    site_type=SiteType.TRAVEL,
    topology=Topology.MATRIX,
    single_page=(
        section("Hero"),
        section("Destination"),
        section("Experiences"),
        section("Highlights"),
        section("Itinerary", required=False),
        section("Accommodation", required=False),
        section("Gallery", required=False),
        section("Reviews", required=False),
        section("FAQ", required=False),
        section("Booking CTA"),
    ),
    multi_page=(
        page(
            "Destinations",
            children=(
                collection(
                    "Destination",
                    children=(
                        page("Overview"),
                        collection("Places", required=False),
                        collection("Experiences", required=False),
                        collection("Accommodation", required=False),
                        collection("Itineraries", required=False),
                    ),
                ),
            ),
        ),
        page(
            "Experiences",
            children=(
                template("Experience"),
                collection("Categories", required=False),
            ),
        ),
        page(
            "Itineraries",
            required=False,
            children=(
                template("Itinerary"),
            ),
        ),
        page("Journal", required=False),
        page("About", required=False),
        page("Contact", required=False),
        page("Booking"),
    ),
    single_page_links=(
        LinkRule("Hero", "Destination", LinkType.NAVIGATION),
        LinkRule("Destination", "Experiences", LinkType.NAVIGATION),
        LinkRule("Experiences", "Highlights", LinkType.NAVIGATION),
        LinkRule("Highlights", "Itinerary", LinkType.NAVIGATION),
        LinkRule("Itinerary", "Accommodation", LinkType.NAVIGATION),
        LinkRule("Accommodation", "Reviews", LinkType.NAVIGATION),
        LinkRule("Reviews", "Booking CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "Booking CTA", LinkType.CTA),
        LinkRule("Experiences", "Booking CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Destinations", LinkType.NAVIGATION),
        LinkRule("Home", "Experiences", LinkType.NAVIGATION),
        LinkRule("Home", "Itineraries", LinkType.NAVIGATION),
        LinkRule("Home", "Journal", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Booking", LinkType.NAVIGATION),
        LinkRule(
            "Destinations.Destination.Experiences",
            "Experiences.Experience",
            LinkType.NAVIGATION,
        ),
        LinkRule(
            "Destinations.Destination.Itineraries",
            "Itineraries.Itinerary",
            LinkType.NAVIGATION,
        ),
        LinkRule(
            "Experiences.Experience",
            "Destinations.Destination",
            LinkType.NAVIGATION,
        ),
        LinkRule(
            "Experiences.Experience",
            "Booking",
            LinkType.CTA,
        ),
        LinkRule(
            "Itineraries.Itinerary",
            "Booking",
            LinkType.CTA,
        ),
        LinkRule("Journal", "Destinations", LinkType.NAVIGATION),
    ),
)


# ---------------------------------------------------------------------------
# Wellness
# ---------------------------------------------------------------------------


WELLNESS = profile(
    site_type=SiteType.WELLNESS,
    topology=Topology.HIERARCHICAL,
    single_page=(
        section("Hero"),
        section("Philosophy"),
        section("Services"),
        section("Programs", required=False),
        section("Benefits", required=False),
        section("Team", required=False),
        section("Testimonials", required=False),
        section("Resources", required=False),
        section("FAQ", required=False),
        section("Booking CTA"),
    ),
    multi_page=(
        page(
            "Services",
            children=(
                template("Service"),
            ),
        ),
        page(
            "Programs",
            required=False,
            children=(
                template("Program"),
            ),
        ),
        page(
            "About",
            children=(
                page("Philosophy", required=False),
                page("Team", required=False),
                page("Approach", required=False),
            ),
        ),
        page(
            "Resources",
            required=False,
            children=(
                page("Blog", required=False),
                page("Guides", required=False),
                page("Articles", required=False),
            ),
        ),
        page("Testimonials", required=False),
        page("Contact"),
    ),
    single_page_links=(
        LinkRule("Hero", "Philosophy", LinkType.NAVIGATION),
        LinkRule("Philosophy", "Services", LinkType.NAVIGATION),
        LinkRule("Services", "Programs", LinkType.NAVIGATION),
        LinkRule("Programs", "Benefits", LinkType.NAVIGATION),
        LinkRule("Benefits", "Testimonials", LinkType.NAVIGATION),
        LinkRule("Testimonials", "FAQ", LinkType.NAVIGATION),
        LinkRule("FAQ", "Booking CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "Booking CTA", LinkType.CTA),
        LinkRule("Services", "Booking CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Services", LinkType.NAVIGATION),
        LinkRule("Home", "Programs", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Resources", LinkType.NAVIGATION),
        LinkRule("Home", "Testimonials", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Services", "Contact", LinkType.CTA),
        LinkRule("Programs", "Contact", LinkType.CTA),
        LinkRule("Resources", "Services", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# Fintech
# ---------------------------------------------------------------------------


FINTECH = profile(
    site_type=SiteType.FINTECH,
    topology=Topology.HIERARCHICAL,
    single_page=(
        section("Hero"),
        section("Product"),
        section("Features"),
        section("Security"),
        section("How It Works"),
        section("Use Cases", required=False),
        section("Integrations", required=False),
        section("Trust"),
        section("Pricing", required=False),
        section("FAQ", required=False),
        section("CTA"),
    ),
    multi_page=(
        page(
            "Product",
            children=(
                page("Overview"),
                page("Features"),
                page("Security"),
                page("Integrations", required=False),
            ),
        ),
        page(
            "Solutions",
            required=False,
            children=(
                page("Individuals"),
                page("Businesses"),
                page("Enterprise"),
            ),
        ),
        page("Pricing", required=False),
        page(
            "Resources",
            required=False,
            children=(
                page("Blog", required=False),
                page("Guides", required=False),
                page("Documentation", required=False),
            ),
        ),
        page(
            "Company",
            required=False,
            children=(
                page("About", required=False),
                page("Careers", required=False),
                page("Contact"),
            ),
        ),
        page("Security"),
        page("Login"),
        page("Signup"),
    ),
    single_page_links=(
        LinkRule("Hero", "Product", LinkType.NAVIGATION),
        LinkRule("Product", "Features", LinkType.NAVIGATION),
        LinkRule("Features", "Security", LinkType.NAVIGATION),
        LinkRule("Security", "How It Works", LinkType.NAVIGATION),
        LinkRule("How It Works", "Use Cases", LinkType.NAVIGATION),
        LinkRule("Use Cases", "Trust", LinkType.NAVIGATION),
        LinkRule("Trust", "Pricing", LinkType.NAVIGATION),
        LinkRule("Pricing", "FAQ", LinkType.NAVIGATION),
        LinkRule("FAQ", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
        LinkRule("Pricing", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Product", LinkType.NAVIGATION),
        LinkRule("Home", "Solutions", LinkType.NAVIGATION),
        LinkRule("Home", "Pricing", LinkType.NAVIGATION),
        LinkRule("Home", "Resources", LinkType.NAVIGATION),
        LinkRule("Home", "Company", LinkType.NAVIGATION),
        LinkRule("Home", "Security", LinkType.NAVIGATION),
        LinkRule("Home", "Login", LinkType.NAVIGATION),
        LinkRule("Product", "Product.Security", LinkType.NAVIGATION),
        LinkRule("Product", "Signup", LinkType.CTA),
        LinkRule("Pricing", "Signup", LinkType.CTA),
        LinkRule("Security", "Signup", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# Technology
# ---------------------------------------------------------------------------


TECHNOLOGY = profile(
    site_type=SiteType.TECHNOLOGY,
    topology=Topology.HIERARCHICAL,
    single_page=(
        section("Hero"),
        section("Technology"),
        section("Features"),
        section("Architecture", required=False),
        section("Use Cases"),
        section("Integrations", required=False),
        section("Performance", required=False),
        section("Security", required=False),
        section("Documentation", required=False),
        section("FAQ", required=False),
        section("CTA"),
    ),
    multi_page=(
        page(
            "Technology",
            children=(
                page("Overview"),
                page("Architecture", required=False),
                page("Features"),
                page("Performance", required=False),
            ),
        ),
        page(
            "Products",
            children=(
                template("Product"),
            ),
        ),
        page(
            "Solutions",
            required=False,
            children=(
                template("Use Case"),
            ),
        ),
        page("Integrations", required=False),
        page("Documentation"),
        page(
            "Resources",
            required=False,
            children=(
                page("Blog", required=False),
                page("Guides", required=False),
                page("Tutorials", required=False),
            ),
        ),
        page(
            "Company",
            required=False,
            children=(
                page("About", required=False),
                page("Careers", required=False),
                page("Contact", required=False),
            ),
        ),
        page("Support", required=False),
    ),
    single_page_links=(
        LinkRule("Hero", "Technology", LinkType.NAVIGATION),
        LinkRule("Technology", "Features", LinkType.NAVIGATION),
        LinkRule("Features", "Architecture", LinkType.NAVIGATION),
        LinkRule("Architecture", "Use Cases", LinkType.NAVIGATION),
        LinkRule("Use Cases", "Integrations", LinkType.NAVIGATION),
        LinkRule("Integrations", "Performance", LinkType.NAVIGATION),
        LinkRule("Performance", "Security", LinkType.NAVIGATION),
        LinkRule("Security", "Documentation", LinkType.NAVIGATION),
        LinkRule("Documentation", "CTA", LinkType.NAVIGATION),
        LinkRule("Hero", "CTA", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Technology", LinkType.NAVIGATION),
        LinkRule("Home", "Products", LinkType.NAVIGATION),
        LinkRule("Home", "Solutions", LinkType.NAVIGATION),
        LinkRule("Home", "Integrations", LinkType.NAVIGATION),
        LinkRule("Home", "Documentation", LinkType.NAVIGATION),
        LinkRule("Home", "Resources", LinkType.NAVIGATION),
        LinkRule("Home", "Company", LinkType.NAVIGATION),
        LinkRule("Home", "Support", LinkType.NAVIGATION),
        LinkRule("Products", "Products.Product", LinkType.NAVIGATION),
        LinkRule("Products.Product", "Documentation", LinkType.CTA),
        LinkRule("Documentation", "Support", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# Fashion
# ---------------------------------------------------------------------------


FASHION = profile(
    site_type=SiteType.FASHION,
    topology=Topology.MATRIX,
    single_page=(
        section("Hero"),
        section("Collection"),
        section("Featured Products"),
        section("Editorial", required=False),
        section("Story", required=False),
        section("Campaign", required=False),
        section("Lookbook", required=False),
        section("Stores", required=False),
        section("Newsletter", required=False),
    ),
    multi_page=(
        page(
            "Collections",
            children=(
                template("Collection"),
            ),
        ),
        page(
            "Shop",
            children=(
                collection(
                    "Category",
                    children=(
                        template("Product"),
                    ),
                ),
            ),
        ),
        page(
            "Editorial",
            required=False,
            children=(
                page("Story", required=False),
                page("Campaign", required=False),
                page("Lookbook", required=False),
            ),
        ),
        page("Journal", required=False),
        page(
            "About",
            children=(
                page("Brand", required=False),
                page("Story", required=False),
                page("Sustainability", required=False),
            ),
        ),
        page("Stores", required=False),
        page("Contact"),
    ),
    single_page_links=(
        LinkRule("Hero", "Collection", LinkType.NAVIGATION),
        LinkRule("Collection", "Featured Products", LinkType.NAVIGATION),
        LinkRule("Featured Products", "Editorial", LinkType.NAVIGATION),
        LinkRule("Editorial", "Story", LinkType.NAVIGATION),
        LinkRule("Story", "Campaign", LinkType.NAVIGATION),
        LinkRule("Campaign", "Lookbook", LinkType.NAVIGATION),
        LinkRule("Lookbook", "Stores", LinkType.NAVIGATION),
        LinkRule("Hero", "Featured Products", LinkType.CTA),
    ),
    multi_page_links=(
        LinkRule("Home", "Collections", LinkType.NAVIGATION),
        LinkRule("Home", "Shop", LinkType.NAVIGATION),
        LinkRule("Home", "Editorial", LinkType.NAVIGATION),
        LinkRule("Home", "Journal", LinkType.NAVIGATION),
        LinkRule("Home", "About", LinkType.NAVIGATION),
        LinkRule("Home", "Stores", LinkType.NAVIGATION),
        LinkRule("Home", "Contact", LinkType.NAVIGATION),
        LinkRule("Collections", "Shop", LinkType.CTA),
        LinkRule("Shop", "Shop.Category.Product", LinkType.NAVIGATION),
        LinkRule("Shop.Category.Product", "Contact", LinkType.CTA),
        LinkRule("Editorial", "Shop", LinkType.CTA),
    ),
)


# ---------------------------------------------------------------------------
# Profile registry
# ---------------------------------------------------------------------------


PROFILES: dict[SiteType, SiteProfile] = {
    site_profile.site_type: site_profile
    for site_profile in (
        LANDING_PAGE,
        SAAS,
        AGENCY,
        PORTFOLIO,
        ECOMMERCE,
        TRAVEL,
        WELLNESS,
        FINTECH,
        TECHNOLOGY,
        FASHION,
    )
}