"""

References
----------
https://www.arista.com/assets/data/pdf/Datasheets/Transceiver-Data-Sheet.pdf
"""

from netcad.helpers import StrEnum


class PhyPortTypes(StrEnum):

    # -------------------------------------------------------------------------
    # 1 Gig
    # -------------------------------------------------------------------------

    type_1000BASE_T = "1000BASE-T"
    type_1000BASE_SX = "1000BASE-SX"
    type_1000BASE_LX = "1000BASE-LX"

    # -------------------------------------------------------------------------
    # 10 Gig
    # -------------------------------------------------------------------------

    type_10GBASE_T = "10GBASE-T"
    type_10GBASE_CR = "10GBASE-CR"
    type_10GBASE_AOC = "10GBASE-AOC"
    type_10GBASE_SR = "10GBASE-SR"
    type_10GBASE_SRL = "10GBASE-SRL"
    type_10GBASE_LR = "10GBASE-LR"
    type_10GBASE_LRL = "10GBASE-LRL"
    type_10GBASE_ER = "10GBASE-ER"
    type_10GBASE_ERLBD = "10GBASE-ERLBD"
    type_10GBASE_ERBD = "10GBASE-ERBD"
    type_10GBASE_ZR = "10GBASE-ZR"
    type_10GBASE_DWDM = "10GBASE-DWDM"

    # -------------------------------------------------------------------------
    # 25 Gig
    # -------------------------------------------------------------------------

    type_25GBASE_CR = "25GBASE-CR"
    type_25GBASE_AOC = "25GBASE-AOC"
    type_25GBASE_SR = "25GBASE-SR"
    type_25GBASE_MR_SR = "25GBASE-MR-SR"
    type_25GBASE_MR_XSR = "25GBASE-MR-XSR"
    type_25GBASE_LR = "25GBASE-LR"
    type_25GBASE_MR_LR = "25GBASE-MR-LR"

    # -------------------------------------------------------------------------
    # 40 Gig
    # -------------------------------------------------------------------------

    type_40GBASE_CR4 = "40GBASE-CR4"
    type_40GBASE_AOC = "40GBASE-AOC"
    type_40GBASE_SR4 = "40GBASE-SR4"
    type_40GBASE_XSR4 = "40GBASE-XSR4"
    type_40GBASE_BIDI = "40GBASE-BIDI"
    type_40GBASE_UNIV = "40GBASE-UNIV"
    type_40GBASE_LR4 = "40GBASE-LR4"
    type_40GBASE_LRL4 = "40GBASE-LRL4"
    type_40GBASE_PLRL4 = "40GBASE-PLRL4"
    type_40GBASE_PLR4 = "40GBASE-PLR4"
    type_40GBASE_ER4 = "40GBASE-ER4"

    # -------------------------------------------------------------------------
    # 100 Gig
    # -------------------------------------------------------------------------

    type_100GBASE_CR4 = "100GBASE-CR4"
    type_100GBASE_AOC = "100GBASE-AOC"
    type_100GBASE_SR4 = "100GBASE-SR4"
    type_100GBASE_XSR4 = "100GBASE-XSR4"
    type_100GBASE_SWDM = "100GBASE-SWDM"
    type_100GBASE_BID = "100GBASE-BID"
    type_100GBASE_PSM4 = "100GBASE-PSM4"
    type_100GBASE_LR4 = "100GBASE-LR4"
    type_100GBASE_LRL4 = "100GBASE-LRL4"
    type_100GBASE_CWDM4 = "100GBASE-CWDM4"
    type_100GBASE_XCWDM4 = "100GBASE-XCWDM4"
    type_100GBASE_ERL4 = "100GBASE-ERL4"
    type_100GBASE_ZR4 = "100GBASE-ZR4"
    type_100GBASE_DR = "100GBASE-DR"
    type_100GBASE_FR = "100GBASE-FR"
    type_100GBASE_LR = "100GBASE-LR"