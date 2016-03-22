﻿from enum import Enum
from core.coordinates import Coordinates
from core.inputfile import Section


# class Node(object):
#     """A node in a SWMM model"""
#     def __init__(self):
#         self.node_id = ''
#         """Node Name"""
#
#         self.centroid = Coordinates(0.0, 0.0)
#         """Coordinates of Node location (x, y)"""
#
#         self.description = None
#         """Optional description of the Node"""
#
#         self.tag = None
#         """Optional label used to categorize or classify the Node"""
#
#         self.direct_inflows = {}
#         """List of external direct, dry weather, or RDII inflows"""
#
#         self.dry_weather_inflows = {}
#         """List of external direct, dry weather, or RDII inflows"""
#
#         self.rdi_inflows = {}
#         """List of external direct, dry weather, or RDII inflows"""
#
#         self.treatments = {}
#         """List of treatment functions for pollutants entering the node"""
#
#         self.invert_elev = None
#         """Invert elevation of the Node (feet or meters)"""


class Junction(Section):
    """A Junction node"""

    field_format = "{:16}\t{:10}\t{:10}\t{:10}\t{:10}\t{}"

    def __init__(self, new_text=None):
        if new_text:
            self.set_text(new_text)
        else:
            Section.__init__(self)

            self.node_id = ''
            """name assigned to junction node"""

            self.elevation = ''
            """Invert elevation of the Node (feet or meters)"""

            self.max_depth = ''
            """Maximum depth of junction (i.e., from ground surface to invert)
                (feet or meters). If zero, then the distance from the invert to
                the top of the highest connecting link will be used.  (Ymax)"""

            self.initial_depth = ''
            """Depth of water at the junction at the start of the simulation
                (feet or meters) (Y0)"""

            self.surcharge_depth = ''
            """Additional depth of water beyond the maximum depth that is
                allowed before the junction floods (feet or meters).
                This parameter can be used to simulate bolted manhole covers
                or force main connections. (Ysur)"""

            self.ponded_area = ''
            """Area occupied by ponded water atop the junction after flooding
                occurs (sq. feet or sq. meters). If the Allow Ponding simulation
                option is turned on, a non-zero value of this parameter will allow
                ponded water to be stored and subsequently returned to the
                conveyance system when capacity exists. (Apond)"""

    def get_text(self):
        """format contents of this item for writing to file"""
        return self.field_format.format(self.node_id, self.elevation,
                                        self.max_depth, self.initial_depth, self.surcharge_depth, self.ponded_area)

    def set_text(self, new_text):
        self.__init__()
        new_text = self.set_comment_check_section(new_text)
        fields = new_text.split()
        if len(fields) > 0:
            self.node_id = fields[0]
        if len(fields) > 1:
            self.elevation = fields[1]
        if len(fields) > 2:
            self.max_depth = fields[2]
        if len(fields) > 3:
            self.initial_depth = fields[3]
        if len(fields) > 4:
            self.surcharge_depth = fields[4]
        if len(fields) > 5:
            self.ponded_area = fields[5]


class OutfallType(Enum):
    """Type of outfall boundary condition:
        FREE: outfall stage determined by minimum of critical flow
                depth and normal flow depth in the connecting conduit
        NORMAL: outfall stage based on normal flow depth in
                connecting conduit
        FIXED: outfall stage set to a fixed value
        TIDAL: outfall stage given by a table of tide elevation versus
                time of day
        TIMESERIES: outfall stage supplied from a time series of elevations.
    """
    FREE = 1
    NORMAL = 2
    FIXED = 3
    TIDAL = 4
    TIMESERIES = 5


class Outfall(Section):
    """A terminal node of the drainage system
        Defines a final downstream boundary under Dynamic Wave flow routing.
        For other types of flow routing they behave as a junction.
        Only a single link can be connected to an outfall node.
        The boundary conditions at an outfall can be described by any one
        of the following stage relationships:
            the critical or normal flow depth in the connecting conduit
            a fixed stage elevation
            a tidal stage described in a table of tide height versus hour
            a user-defined time series of stage versus time.
        The principal input parameters for outfalls include:
            invert elevation
            boundary condition type and stage description
            presence of a flap gate to prevent backflow through the outfall.
    """
    def __init__(self):
        Section.__init__(self)

        self.tide_gate = False
        """Tide Gate is present to prevent backflow"""

        self.outfall_type = OutfallType.FREE
        """Type of outfall boundary condition"""

        self.fixed_stage = 0.0
        """Water elevation for a FIXED type of outfall (feet or meters)."""

        self.tidal_curve = None
        """The TidalCurve relating water elevation to hour of the
            day for a TIDAL outfall."""

        self.time_series_name = None
        """Name of time series containing time history of outfall elevations
            for a TIMESERIES outfall"""


class FlowDividerType(Enum):
    """Type of flow divider. Choices are:
        CUTOFF (diverts all inflow above a defined cutoff value),
        OVERFLOW (diverts all inflow above the flow capacity of the
                non-diverted link),
        TABULAR (uses a Diversion Curve to express diverted flow as a
                function of the total inflow),
        WEIR (uses a weir equation to compute diverted flow).
    """
    CUTOFF = 1
    OVERFLOW = 2
    TABULAR = 3
    WEIR = 4


class WeirDivider:
    def __init__(self):
        self.min_flow = 0.0
        """Minimum flow at which diversion begins (flow units)."""

        self.max_depth = 0.0
        """Vertical height of WEIR opening (feet or meters)"""

        self.coefficient = 0.0
        """Product of WEIR's discharge coefficient and its length.
            Weir coefficients are typically in the range of
            2.65 to 3.10 per foot, for flows in CFS."""


class Divider(Junction):
    """Flow Dividers are drainage system nodes that divert inflows to
        a specific conduit in a prescribed manner. A flow divider can
        have no more than two conduit links on its discharge side.
        Flow dividers are only active under Kinematic Wave routing
        and are treated as simple junctions under Dynamic Wave routing.
    """
    def __init__(self):
        Junction.__init__(self)

        self.diverted_link = None
        """Name of link which receives the diverted flow."""

        self.flow_divider_type = FlowDividerType.CUTOFF
        """Type of flow divider from FlowDividerType(Enum)"""

        self.max_depth = 0.0
        """Maximum depth of node (i.e., from ground surface to invert)
            (feet or meters). If zero, then the distance from the invert to
            the top of the highest connecting link will be used. """

        self.initial_depth = 0.0
        """Depth of water at the node at the start of the simulation
            (feet or meters)."""

        self.surcharge_depth = 0.0
        """Additional depth of water beyond the maximum depth that is
            allowed before the node floods (feet or meters).
            This parameter can be used to simulate bolted manhole covers
            or force main connections. """

        self.ponded_area = 0.0
        """Area occupied by ponded water atop the node after flooding
            occurs (sq. feet or sq. meters). If the Allow Ponding simulation
            option is turned on, a non-zero value of this parameter will allow
            ponded water to be stored and subsequently returned to the
            conveyance system when capacity exists."""

        self.cutoff_flow = 0
        """Cutoff flow value used for a CUTOFF divider (flow units)."""

        self.divider_curve = None
        """Diversion Curve used with a TABULAR divider"""

        self.weir = None
        """WeirDivider used with a WEIR divider"""


class StorageCurveType(Enum):
    FUNCTIONAL = 1
    TABULAR = 2


class StorageUnit(Junction):
    """Storage Units are drainage system nodes that provide storage volume.
        Physically they could represent storage facilities as small as
        a catch basin or as large as a lake. The volumetric properties
        of a storage unit are described by a function or table of
        surface area versus height.
    """
    def __init__(self):
        Junction.__init__(self)
        self.max_depth = ''
        """Maximum depth of node (i.e., from ground surface to invert)
            (feet or meters). If zero, then the distance from the invert to
            the top of the highest connecting link will be used. """

        self.initial_depth = ''
        """Depth of water at the node at the start of the simulation
            (feet or meters)."""

        self.storage_curve_type = StorageCurveType.TABULAR
        """StorageCurveType: FUNCTIONAL or TABULAR"""

        self.storage_curve = ''
        """Storage Curve containing the relationship between
            surface area and storage depth"""

        self.coefficient = ''
        """A-value in the functional relationship
            between surface area and storage depth."""

        self.exponent = ''
        """B-value in the functional relationship
            between surface area and storage depth."""

        self.constant = ''
        """C-value in the functional relationship
            between surface area and storage depth."""

        self.ponded_area = ''
        """Area occupied by ponded water atop the node after flooding
            occurs (sq. feet or sq. meters). If the Allow Ponding simulation
            option is turned on, a non-zero value of this parameter will allow
            ponded water to be stored and subsequently returned to the
            conveyance system when capacity exists."""

        self.evaporation_factor = ''
        """The fraction of the potential evaporation from the storage units
            water surface that is actually realized."""

        self.seepage_loss = ''
        """The following Green-Ampt infiltration parameters are only used when the storage
            node is intended to act as an infiltration basin:"""

        self.seepage_suction_head = ''
        """Soil capillary suction head (in or mm)."""

        self.seepage_hydraulic_conductivity = ''
        """Soil saturated hydraulic conductivity (in/hr or mm/hr)."""

        self.seepage_initial_moisture_deficit = ''
        """Initial soil moisture deficit (volume of voids / total volume)."""


class DirectInflowType(Enum):
    CONCENTRATION = 1
    MASS = 2


class DirectInflow:
    """Defines characteristics of direct inflows added directly into a node"""
    def __init__(self):
        self.constituent = ''
        """str: Name of constituent"""

        self.timeseries = ''
        """str: Name of the time series that contains inflow data for the selected constituent"""

        self.format = DirectInflowType.CONCENTRATION
        """DirectInflowType: Type of inflow data contained in the time series, concentration or mass flow rate"""

        self.conversion_factor = ''
        """float: Numerical factor used to convert the units of pollutant mass flow rate in the time series data
        into concentration mass units per second"""

        self.scale_factor = ''
        """float: Multiplier used to adjust the values of the constituent's inflow time series"""

        self.baseline = ''
        """float: Value of the constant baseline component of the constituent's inflow"""

        self.baseline_pattern = ''
        """str: ID of Time Pattern whose factors adjust the baseline inflow on an hourly, daily, or monthly basis"""


class DryWeatherInflow:
    """Defines characteristics of dry weather inflows added to a node"""
    def __init__(self):
        self.constituent = ""
        """str: Name of constituent"""

        self.average = 0.0
        """float: Average (or baseline) value of the dry weather inflow of the constituent in the relevant units"""

        self.time_pattern = ""    # (Subclass Pattern)
        """str: ID of time pattern used to allow the dry weather flow to vary in a periodic fashion"""


class RDIInflow:
    """Defines characteristics of Rainfall-Dependent Infiltration/Inflows at a node"""
    def __init__(self):
        self.hydrograph_group = ""
        """str: name of an RDII unit hydrograph group specified in the [HYDROGRAPHS] section"""

        self.sewershed_area = 0.0
        """float: area of the sewershed which contributes RDII to the node (acres or hectares)"""


class TreatmentResult(Enum):
    CONCENTRATION = 1
    REMOVAL = 2


class Treatment:
    """Define the treatment properties of a node using a treatment expression"""
    def __init__(self):
        self.pollutant = ""
        """Name of pollutant receiving treatment"""

        self.result = TreatmentResult.CONCENTRATION
        """TreatmentResult: Result computed by treatment function. Choices are:
        C function computes effluent concentration
        R function computes fractional removal."""

        self.function = ""
        """str: mathematical function expressing treatment result in terms of pollutant concentrations,
        pollutant removals, and other standard variables"""
