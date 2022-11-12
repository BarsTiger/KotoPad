# source: https://github.com/Opticos/GWSL-Source/blob/master/blur.py,
# https://www.cnblogs.com/zhiyiYo/p/14659981.html ,
# https://github.com/ifwe/digsby/blob/master/digsby/src/gui/vista.py
import platform
import ctypes


if platform.system() == 'Windows':
    from ctypes.wintypes import DWORD, BOOL, HRGN, HWND

    user32 = ctypes.windll.user32
    dwm = ctypes.windll.dwmapi


    class ACCENTPOLICY(ctypes.Structure):
        _fields_ = [
            ("AccentState", ctypes.c_uint),
            ("AccentFlags", ctypes.c_uint),
            ("GradientColor", ctypes.c_uint),
            ("AnimationId", ctypes.c_uint)
        ]


    class WINDOWCOMPOSITIONATTRIBDATA(ctypes.Structure):
        _fields_ = [
            ("Attribute", ctypes.c_int),
            ("Data", ctypes.POINTER(ctypes.c_int)),
            ("SizeOfData", ctypes.c_size_t)
        ]


    class DWM_BLURBEHIND(ctypes.Structure):
        _fields_ = [
            ('dwFlags', DWORD),
            ('fEnable', BOOL),
            ('hRgnBlur', HRGN),
            ('fTransitionOnMaximized', BOOL)
        ]


    class MARGINS(ctypes.Structure):
        _fields_ = [("cxLeftWidth", ctypes.c_int),
                    ("cxRightWidth", ctypes.c_int),
                    ("cyTopHeight", ctypes.c_int),
                    ("cyBottomHeight", ctypes.c_int)
                    ]


    SetWindowCompositionAttribute = user32.SetWindowCompositionAttribute
    SetWindowCompositionAttribute.argtypes = (HWND, WINDOWCOMPOSITIONATTRIBDATA)
    SetWindowCompositionAttribute.restype = ctypes.c_int


def ExtendFrameIntoClientArea(hwnd):
    margins = MARGINS(-1, -1, -1, -1)
    dwm.DwmExtendFrameIntoClientArea(hwnd, ctypes.byref(margins))


def Win7Blur(hwnd, Acrylic):
    if not Acrylic:
        DWM_BB_ENABLE = 0x01
        bb = DWM_BLURBEHIND()
        bb.dwFlags = DWM_BB_ENABLE
        bb.fEnable = 1
        bb.hRgnBlur = 1
        dwm.DwmEnableBlurBehindWindow(hwnd, ctypes.byref(bb))
    else:
        ExtendFrameIntoClientArea(hwnd)


def HEXtoRGBAint(HEX: str):
    alpha = HEX[7:]
    blue = HEX[5:7]
    green = HEX[3:5]
    red = HEX[1:3]

    gradient_color = alpha + blue + green + red
    return int(gradient_color, base=16)


def blur(hwnd, hex_color=False, acrylic=False, dark=False):
    accent = ACCENTPOLICY()
    accent.AccentState = 3  # Default window Blur #ACCENT_ENABLE_BLURBEHIND

    gradient_color = 0

    if hex_color:
        gradient_color = HEXtoRGBAint(hex_color)
        accent.AccentFlags = 2  # Window Blur With Accent Color #ACCENT_ENABLE_TRANSPARENTGRADIENT

    if acrylic:
        accent.AccentState = 4  # UWP but LAG #ACCENT_ENABLE_ACRYLICBLURBEHIND
        if not hex_color:  # UWP without color is translucent
            accent.AccentFlags = 2
            gradient_color = HEXtoRGBAint('#12121240')  # placeholder color

    accent.GradientColor = gradient_color

    data = WINDOWCOMPOSITIONATTRIBDATA()
    data.Attribute = 19  # WCA_ACCENT_POLICY
    data.SizeOfData = ctypes.sizeof(accent)
    data.Data = ctypes.cast(ctypes.pointer(accent), ctypes.POINTER(ctypes.c_int))

    SetWindowCompositionAttribute(int(hwnd), data)

    if dark:
        data.Attribute = 26  # WCA_USEDARKMODECOLORS
        SetWindowCompositionAttribute(int(hwnd), data)


def BlurLinux(WID):  # may not work in all distros (working in Deepin)
    import os

    c = "xprop -f _KDE_NET_WM_BLUR_BEHIND_REGION 32c -set _KDE_NET_WM_BLUR_BEHIND_REGION 0 -id " + str(WID)
    os.system(c)


def GlobalBlur(hwnd, hex_color=False, acrylic=False, dark=False):
    release = platform.release()
    system = platform.system()

    if system == 'Windows':
        if release == 'Vista':
            Win7Blur(hwnd, acrylic)
        else:
            release = int(float(release))
            if release == 10 or release == 8 or release == 11:
                blur(hwnd, hex_color, acrylic, dark)
            else:
                Win7Blur(hwnd, acrylic)

    if system == 'Linux':
        BlurLinux(hwnd)
