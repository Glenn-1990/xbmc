# -*- coding: utf-8 -*-
# Copyright (C) 2005-2006  Joe Wreschnig
# Copyright (C) 2006-2007  Lukas Lalinsky
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

import struct

from mutagen._util import MutagenError


class error(IOError, MutagenError):
    """Error raised by :mod:`mutagen.asf`"""


class ASFError(error):
    pass


class ASFHeaderError(error):
    pass


def guid2bytes(s):
    """Converts a GUID to the serialized bytes representation"""

    assert isinstance(s, str)
    assert len(s) == 36

    p = struct.pack
    return b"".join([
        p("<IHH", int(s[:8], 16), int(s[9:13], 16), int(s[14:18], 16)),
        p(">H", int(s[19:23], 16)),
        p(">Q", int(s[24:], 16))[2:],
        ])


def bytes2guid(s):
    """Converts a serialized GUID to a text GUID"""

    assert isinstance(s, bytes)

    u = struct.unpack
    v = []
    v.extend(u("<IHH", s[:8]))
    v.extend(u(">HQ", s[8:10] + b"\x00\x00" + s[10:]))
    return "%08X-%04X-%04X-%04X-%012X" % tuple(v)


# Names from http://windows.microsoft.com/en-za/windows7/c00d10d1-[0-9A-F]{1,4}
CODECS = {
    0x0000: u"Unknown Wave Format",
    0x0001: u"Microsoft PCM Format",
    0x0002: u"Microsoft ADPCM Format",
    0x0003: u"IEEE Float",
    0x0004: u"Compaq Computer VSELP",
    0x0005: u"IBM CVSD",
    0x0006: u"Microsoft CCITT A-Law",
    0x0007: u"Microsoft CCITT u-Law",
    0x0008: u"Microsoft DTS",
    0x0009: u"Microsoft DRM",
    0x000A: u"Windows Media Audio 9 Voice",
    0x000B: u"Windows Media Audio 10 Voice",
    0x000C: u"OGG Vorbis",
    0x000D: u"FLAC",
    0x000E: u"MOT AMR",
    0x000F: u"Nice Systems IMBE",
    0x0010: u"OKI ADPCM",
    0x0011: u"Intel IMA ADPCM",
    0x0012: u"Videologic MediaSpace ADPCM",
    0x0013: u"Sierra Semiconductor ADPCM",
    0x0014: u"Antex Electronics G.723 ADPCM",
    0x0015: u"DSP Solutions DIGISTD",
    0x0016: u"DSP Solutions DIGIFIX",
    0x0017: u"Dialogic OKI ADPCM",
    0x0018: u"MediaVision ADPCM",
    0x0019: u"Hewlett-Packard CU codec",
    0x001A: u"Hewlett-Packard Dynamic Voice",
    0x0020: u"Yamaha ADPCM",
    0x0021: u"Speech Compression SONARC",
    0x0022: u"DSP Group True Speech",
    0x0023: u"Echo Speech EchoSC1",
    0x0024: u"Ahead Inc. Audiofile AF36",
    0x0025: u"Audio Processing Technology APTX",
    0x0026: u"Ahead Inc. AudioFile AF10",
    0x0027: u"Aculab Prosody 1612",
    0x0028: u"Merging Technologies S.A. LRC",
    0x0030: u"Dolby Labs AC2",
    0x0031: u"Microsoft GSM 6.10",
    0x0032: u"Microsoft MSNAudio",
    0x0033: u"Antex Electronics ADPCME",
    0x0034: u"Control Resources VQLPC",
    0x0035: u"DSP Solutions Digireal",
    0x0036: u"DSP Solutions DigiADPCM",
    0x0037: u"Control Resources CR10",
    0x0038: u"Natural MicroSystems VBXADPCM",
    0x0039: u"Crystal Semiconductor IMA ADPCM",
    0x003A: u"Echo Speech EchoSC3",
    0x003B: u"Rockwell ADPCM",
    0x003C: u"Rockwell DigiTalk",
    0x003D: u"Xebec Multimedia Solutions",
    0x0040: u"Antex Electronics G.721 ADPCM",
    0x0041: u"Antex Electronics G.728 CELP",
    0x0042: u"Intel G.723",
    0x0043: u"Intel G.723.1",
    0x0044: u"Intel G.729 Audio",
    0x0045: u"Sharp G.726 Audio",
    0x0050: u"Microsoft MPEG-1",
    0x0052: u"InSoft RT24",
    0x0053: u"InSoft PAC",
    0x0055: u"MP3 - MPEG Layer III",
    0x0059: u"Lucent G.723",
    0x0060: u"Cirrus Logic",
    0x0061: u"ESS Technology ESPCM",
    0x0062: u"Voxware File-Mode",
    0x0063: u"Canopus Atrac",
    0x0064: u"APICOM G.726 ADPCM",
    0x0065: u"APICOM G.722 ADPCM",
    0x0066: u"Microsoft DSAT",
    0x0067: u"Microsoft DSAT Display",
    0x0069: u"Voxware Byte Aligned",
    0x0070: u"Voxware AC8",
    0x0071: u"Voxware AC10",
    0x0072: u"Voxware AC16",
    0x0073: u"Voxware AC20",
    0x0074: u"Voxware RT24 MetaVoice",
    0x0075: u"Voxware RT29 MetaSound",
    0x0076: u"Voxware RT29HW",
    0x0077: u"Voxware VR12",
    0x0078: u"Voxware VR18",
    0x0079: u"Voxware TQ40",
    0x007A: u"Voxware SC3",
    0x007B: u"Voxware SC3",
    0x0080: u"Softsound",
    0x0081: u"Voxware TQ60",
    0x0082: u"Microsoft MSRT24",
    0x0083: u"AT&T Labs G.729A",
    0x0084: u"Motion Pixels MVI MV12",
    0x0085: u"DataFusion Systems G.726",
    0x0086: u"DataFusion Systems GSM610",
    0x0088: u"Iterated Systems ISIAudio",
    0x0089: u"Onlive",
    0x008A: u"Multitude FT SX20",
    0x008B: u"Infocom ITS ACM G.721",
    0x008C: u"Convedia G.729",
    0x008D: u"Congruency Audio",
    0x0091: u"Siemens Business Communications SBC24",
    0x0092: u"Sonic Foundry Dolby AC3 SPDIF",
    0x0093: u"MediaSonic G.723",
    0x0094: u"Aculab Prosody 8KBPS",
    0x0097: u"ZyXEL ADPCM",
    0x0098: u"Philips LPCBB",
    0x0099: u"Studer Professional Audio AG Packed",
    0x00A0: u"Malden Electronics PHONYTALK",
    0x00A1: u"Racal Recorder GSM",
    0x00A2: u"Racal Recorder G720.a",
    0x00A3: u"Racal Recorder G723.1",
    0x00A4: u"Racal Recorder Tetra ACELP",
    0x00B0: u"NEC AAC",
    0x00FF: u"CoreAAC Audio",
    0x0100: u"Rhetorex ADPCM",
    0x0101: u"BeCubed Software IRAT",
    0x0111: u"Vivo G.723",
    0x0112: u"Vivo Siren",
    0x0120: u"Philips CELP",
    0x0121: u"Philips Grundig",
    0x0123: u"Digital G.723",
    0x0125: u"Sanyo ADPCM",
    0x0130: u"Sipro Lab Telecom ACELP.net",
    0x0131: u"Sipro Lab Telecom ACELP.4800",
    0x0132: u"Sipro Lab Telecom ACELP.8V3",
    0x0133: u"Sipro Lab Telecom ACELP.G.729",
    0x0134: u"Sipro Lab Telecom ACELP.G.729A",
    0x0135: u"Sipro Lab Telecom ACELP.KELVIN",
    0x0136: u"VoiceAge AMR",
    0x0140: u"Dictaphone G.726 ADPCM",
    0x0141: u"Dictaphone CELP68",
    0x0142: u"Dictaphone CELP54",
    0x0150: u"Qualcomm PUREVOICE",
    0x0151: u"Qualcomm HALFRATE",
    0x0155: u"Ring Zero Systems TUBGSM",
    0x0160: u"Windows Media Audio Standard",
    0x0161: u"Windows Media Audio 9 Standard",
    0x0162: u"Windows Media Audio 9 Professional",
    0x0163: u"Windows Media Audio 9 Lossless",
    0x0164: u"Windows Media Audio Pro over SPDIF",
    0x0170: u"Unisys NAP ADPCM",
    0x0171: u"Unisys NAP ULAW",
    0x0172: u"Unisys NAP ALAW",
    0x0173: u"Unisys NAP 16K",
    0x0174: u"Sycom ACM SYC008",
    0x0175: u"Sycom ACM SYC701 G725",
    0x0176: u"Sycom ACM SYC701 CELP54",
    0x0177: u"Sycom ACM SYC701 CELP68",
    0x0178: u"Knowledge Adventure ADPCM",
    0x0180: u"Fraunhofer IIS MPEG-2 AAC",
    0x0190: u"Digital Theater Systems DTS",
    0x0200: u"Creative Labs ADPCM",
    0x0202: u"Creative Labs FastSpeech8",
    0x0203: u"Creative Labs FastSpeech10",
    0x0210: u"UHER informatic GmbH ADPCM",
    0x0215: u"Ulead DV Audio",
    0x0216: u"Ulead DV Audio",
    0x0220: u"Quarterdeck",
    0x0230: u"I-link Worldwide ILINK VC",
    0x0240: u"Aureal Semiconductor RAW SPORT",
    0x0249: u"Generic Passthru",
    0x0250: u"Interactive Products HSX",
    0x0251: u"Interactive Products RPELP",
    0x0260: u"Consistent Software CS2",
    0x0270: u"Sony SCX",
    0x0271: u"Sony SCY",
    0x0272: u"Sony ATRAC3",
    0x0273: u"Sony SPC",
    0x0280: u"Telum Audio",
    0x0281: u"Telum IA Audio",
    0x0285: u"Norcom Voice Systems ADPCM",
    0x0300: u"Fujitsu TOWNS SND",
    0x0350: u"Micronas SC4 Speech",
    0x0351: u"Micronas CELP833",
    0x0400: u"Brooktree BTV Digital",
    0x0401: u"Intel Music Coder",
    0x0402: u"Intel Audio",
    0x0450: u"QDesign Music",
    0x0500: u"On2 AVC0 Audio",
    0x0501: u"On2 AVC1 Audio",
    0x0680: u"AT&T Labs VME VMPCM",
    0x0681: u"AT&T Labs TPC",
    0x08AE: u"ClearJump Lightwave Lossless",
    0x1000: u"Olivetti GSM",
    0x1001: u"Olivetti ADPCM",
    0x1002: u"Olivetti CELP",
    0x1003: u"Olivetti SBC",
    0x1004: u"Olivetti OPR",
    0x1100: u"Lernout & Hauspie",
    0x1101: u"Lernout & Hauspie CELP",
    0x1102: u"Lernout & Hauspie SBC8",
    0x1103: u"Lernout & Hauspie SBC12",
    0x1104: u"Lernout & Hauspie SBC16",
    0x1400: u"Norris Communication",
    0x1401: u"ISIAudio",
    0x1500: u"AT&T Labs Soundspace Music Compression",
    0x1600: u"Microsoft MPEG ADTS AAC",
    0x1601: u"Microsoft MPEG RAW AAC",
    0x1608: u"Nokia MPEG ADTS AAC",
    0x1609: u"Nokia MPEG RAW AAC",
    0x181C: u"VoxWare MetaVoice RT24",
    0x1971: u"Sonic Foundry Lossless",
    0x1979: u"Innings Telecom ADPCM",
    0x1FC4: u"NTCSoft ALF2CD ACM",
    0x2000: u"Dolby AC3",
    0x2001: u"DTS",
    0x4143: u"Divio AAC",
    0x4201: u"Nokia Adaptive Multi-Rate",
    0x4243: u"Divio G.726",
    0x4261: u"ITU-T H.261",
    0x4263: u"ITU-T H.263",
    0x4264: u"ITU-T H.264",
    0x674F: u"Ogg Vorbis Mode 1",
    0x6750: u"Ogg Vorbis Mode 2",
    0x6751: u"Ogg Vorbis Mode 3",
    0x676F: u"Ogg Vorbis Mode 1+",
    0x6770: u"Ogg Vorbis Mode 2+",
    0x6771: u"Ogg Vorbis Mode 3+",
    0x7000: u"3COM NBX Audio",
    0x706D: u"FAAD AAC Audio",
    0x77A1: u"True Audio Lossless Audio",
    0x7A21: u"GSM-AMR CBR 3GPP Audio",
    0x7A22: u"GSM-AMR VBR 3GPP Audio",
    0xA100: u"Comverse Infosys G723.1",
    0xA101: u"Comverse Infosys AVQSBC",
    0xA102: u"Comverse Infosys SBC",
    0xA103: u"Symbol Technologies G729a",
    0xA104: u"VoiceAge AMR WB",
    0xA105: u"Ingenient Technologies G.726",
    0xA106: u"ISO/MPEG-4 Advanced Audio Coding (AAC)",
    0xA107: u"Encore Software Ltd's G.726",
    0xA108: u"ZOLL Medical Corporation ASAO",
    0xA109: u"Speex Voice",
    0xA10A: u"Vianix MASC Speech Compression",
    0xA10B: u"Windows Media 9 Spectrum Analyzer Output",
    0xA10C: u"Media Foundation Spectrum Analyzer Output",
    0xA10D: u"GSM 6.10 (Full-Rate) Speech",
    0xA10E: u"GSM 6.20 (Half-Rate) Speech",
    0xA10F: u"GSM 6.60 (Enchanced Full-Rate) Speech",
    0xA110: u"GSM 6.90 (Adaptive Multi-Rate) Speech",
    0xA111: u"GSM Adaptive Multi-Rate WideBand Speech",
    0xA112: u"Polycom G.722",
    0xA113: u"Polycom G.728",
    0xA114: u"Polycom G.729a",
    0xA115: u"Polycom Siren",
    0xA116: u"Global IP Sound ILBC",
    0xA117: u"Radio Time Time Shifted Radio",
    0xA118: u"Nice Systems ACA",
    0xA119: u"Nice Systems ADPCM",
    0xA11A: u"Vocord Group ITU-T G.721",
    0xA11B: u"Vocord Group ITU-T G.726",
    0xA11C: u"Vocord Group ITU-T G.722.1",
    0xA11D: u"Vocord Group ITU-T G.728",
    0xA11E: u"Vocord Group ITU-T G.729",
    0xA11F: u"Vocord Group ITU-T G.729a",
    0xA120: u"Vocord Group ITU-T G.723.1",
    0xA121: u"Vocord Group LBC",
    0xA122: u"Nice G.728",
    0xA123: u"France Telecom G.729 ACM Audio",
    0xA124: u"CODIAN Audio",
    0xCC12: u"Intel YUV12 Codec",
    0xCFCC: u"Digital Processing Systems Perception Motion JPEG",
    0xD261: u"DEC H.261",
    0xD263: u"DEC H.263",
    0xFFFE: u"Extensible Wave Format",
    0xFFFF: u"Unregistered",
}
