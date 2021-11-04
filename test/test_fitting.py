import numpy as np
from hillfit import HillFit


def test_plot():
    x_data = [
        9.210, 10.210, 10.580, 10.830, 11.080,
        11.330, 11.580, 11.830, 12.080, 12.330,
        12.580, 12.830, 13.080, 13.330, 13.580,
        13.830, 14.080, 14.330, 14.580, 14.830,
        15.080, 15.330, 15.580, 15.830, 17.580
    ]
    y_data = [
        0.000, 0.000, 0.000, 1.667, 2.222,
        5.682, 9.524, 15.315, 16.000, 31.183,
        39.000, 47.222, 47.475, 63.208, 77.143,
        75.214, 80.612, 92.784, 94.167, 93.137,
        95.902, 96.396, 97.872, 98.246, 100.000
    ]
    model = HillFit(x_data, y_data)
    x_fit, y_fit = model.fitting()
    assert np.allclose(
        x_fit,
        [
            9.21      ,  9.2159619 ,  9.22192765,  9.22789727,  9.23387075,
            9.2398481 ,  9.24582932,  9.25181441,  9.25780337,  9.26379621,
            9.26979293,  9.27579353,  9.28179802,  9.28780639,  9.29381866,
            9.29983481,  9.30585486,  9.31187881,  9.31790665,  9.3239384 ,
            9.32997405,  9.33601361,  9.34205708,  9.34810446,  9.35415575,
            9.36021097,  9.3662701 ,  9.37233315,  9.37840013,  9.38447104,
            9.39054587,  9.39662464,  9.40270735,  9.40879399,  9.41488457,
            9.42097909,  9.42707756,  9.43317998,  9.43928635,  9.44539667,
            9.45151094,  9.45762917,  9.46375137,  9.46987753,  9.47600765,
            9.48214174,  9.4882798 ,  9.49442183,  9.50056785,  9.50671783,
            9.5128718 ,  9.51902976,  9.5251917 ,  9.53135763,  9.53752755,
            9.54370146,  9.54987937,  9.55606128,  9.56224719,  9.56843711,
            9.57463103,  9.58082897,  9.58703091,  9.59323687,  9.59944685,
            9.60566084,  9.61187886,  9.6181009 ,  9.62432698,  9.63055708,
            9.63679121,  9.64302938,  9.64927159,  9.65551784,  9.66176813,
            9.66802247,  9.67428086,  9.6805433 ,  9.68680979,  9.69308034,
            9.69935495,  9.70563362,  9.71191635,  9.71820315,  9.72449402,
            9.73078897,  9.73708799,  9.74339108,  9.74969826,  9.75600951,
            9.76232486,  9.76864429,  9.77496781,  9.78129543,  9.78762714,
            9.79396295,  9.80030286,  9.80664688,  9.812995  ,  9.81934724,
            9.82570358,  9.83206404,  9.83842861,  9.84479731,  9.85117013,
            9.85754707,  9.86392815,  9.87031335,  9.87670268,  9.88309616,
            9.88949377,  9.89589552,  9.90230142,  9.90871146,  9.91512565,
            9.92154399,  9.92796649,  9.93439315,  9.94082397,  9.94725895,
            9.95369809,  9.9601414 ,  9.96658889,  9.97304055,  9.97949638,
            9.98595639,  9.99242059,  9.99888897, 10.00536154, 10.01183829,
            10.01831924, 10.02480439, 10.03129373, 10.03778727, 10.04428502,
            10.05078697, 10.05729313, 10.06380351, 10.07031809, 10.0768369 ,
            10.08335992, 10.08988717, 10.09641864, 10.10295434, 10.10949427,
            10.11603844, 10.12258684, 10.12913948, 10.13569636, 10.14225749,
            10.14882286, 10.15539248, 10.16196636, 10.16854449, 10.17512688,
            10.18171353, 10.18830445, 10.19489963, 10.20149908, 10.2081028 ,
            10.21471079, 10.22132307, 10.22793962, 10.23456046, 10.24118559,
            10.247815  , 10.2544487 , 10.2610867 , 10.26772899, 10.27437559,
            10.28102648, 10.28768169, 10.2943412 , 10.30100502, 10.30767315,
            10.31434561, 10.32102238, 10.32770347, 10.33438889, 10.34107863,
            10.34777271, 10.35447112, 10.36117386, 10.36788095, 10.37459237,
            10.38130814, 10.38802826, 10.39475273, 10.40148155, 10.40821472,
            10.41495226, 10.42169416, 10.42844042, 10.43519104, 10.44194604,
            10.44870541, 10.45546916, 10.46223728, 10.46900979, 10.47578668,
            10.48256795, 10.48935362, 10.49614368, 10.50293813, 10.50973698,
            10.51654024, 10.52334789, 10.53015996, 10.53697643, 10.54379732,
            10.55062262, 10.55745234, 10.56428648, 10.57112504, 10.57796803,
            10.58481546, 10.59166731, 10.5985236 , 10.60538433, 10.61224949,
            10.61911911, 10.62599317, 10.63287168, 10.63975464, 10.64664205,
            10.65353393, 10.66043027, 10.66733107, 10.67423634, 10.68114608,
            10.68806029, 10.69497897, 10.70190214, 10.70882979, 10.71576192,
            10.72269854, 10.72963965, 10.73658525, 10.74353535, 10.75048994,
            10.75744904, 10.76441265, 10.77138076, 10.77835338, 10.78533052,
            10.79231217, 10.79929834, 10.80628904, 10.81328426, 10.82028401,
            10.82728829, 10.8342971 , 10.84131045, 10.84832834, 10.85535077,
            10.86237775, 10.86940928, 10.87644536, 10.88348599, 10.89053118,
            10.89758094, 10.90463525, 10.91169413, 10.91875759, 10.92582561,
            10.93289821, 10.93997539, 10.94705715, 10.95414349, 10.96123442,
            10.96832994, 10.97543005, 10.98253476, 10.98964407, 10.99675798,
            11.0038765 , 11.01099962, 11.01812736, 11.02525971, 11.03239667,
            11.03953826, 11.04668447, 11.0538353 , 11.06099076, 11.06815086,
            11.07531559, 11.08248496, 11.08965897, 11.09683762, 11.10402092,
            11.11120887, 11.11840147, 11.12559873, 11.13280065, 11.14000723,
            11.14721848, 11.15443439, 11.16165497, 11.16888023, 11.17611017,
            11.18334478, 11.19058408, 11.19782807, 11.20507674, 11.21233011,
            11.21958817, 11.22685093, 11.23411839, 11.24139056, 11.24866743,
            11.25594902, 11.26323531, 11.27052633, 11.27782206, 11.28512252,
            11.2924277 , 11.29973761, 11.30705225, 11.31437163, 11.32169575,
            11.32902461, 11.33635821, 11.34369656, 11.35103966, 11.35838751,
            11.36574012, 11.37309749, 11.38045962, 11.38782651, 11.39519818,
            11.40257462, 11.40995583, 11.41734182, 11.42473259, 11.43212815,
            11.43952849, 11.44693362, 11.45434355, 11.46175828, 11.4691778 ,
            11.47660213, 11.48403126, 11.4914652 , 11.49890395, 11.50634752,
            11.51379591, 11.52124912, 11.52870715, 11.53617002, 11.54363771,
            11.55111024, 11.5585876 , 11.5660698 , 11.57355685, 11.58104875,
            11.58854549, 11.59604709, 11.60355354, 11.61106485, 11.61858103,
            11.62610207, 11.63362797, 11.64115875, 11.64869441, 11.65623494,
            11.66378036, 11.67133065, 11.67888584, 11.68644592, 11.69401089,
            11.70158075, 11.70915552, 11.71673519, 11.72431977, 11.73190926,
            11.73950366, 11.74710297, 11.75470721, 11.76231637, 11.76993045,
            11.77754946, 11.78517341, 11.79280229, 11.80043611, 11.80807487,
            11.81571857, 11.82336722, 11.83102083, 11.83867938, 11.8463429 ,
            11.85401138, 11.86168482, 11.86936323, 11.8770466 , 11.88473495,
            11.89242828, 11.90012659, 11.90782988, 11.91553816, 11.92325143,
            11.93096969, 11.93869295, 11.94642121, 11.95415447, 11.96189273,
            11.96963601, 11.9773843 , 11.9851376 , 11.99289592, 12.00065927,
            12.00842764, 12.01620104, 12.02397947, 12.03176293, 12.03955144,
            12.04734498, 12.05514357, 12.06294721, 12.0707559 , 12.07856965,
            12.08638845, 12.09421232, 12.10204124, 12.10987524, 12.11771431,
            12.12555845, 12.13340767, 12.14126198, 12.14912136, 12.15698584,
            12.1648554 , 12.17273006, 12.18060981, 12.18849467, 12.19638463,
            12.2042797 , 12.21217988, 12.22008517, 12.22799558, 12.23591111,
            12.24383177, 12.25175755, 12.25968846, 12.26762451, 12.2755657 ,
            12.28351202, 12.29146349, 12.2994201 , 12.30738187, 12.31534879,
            12.32332087, 12.33129811, 12.33928051, 12.34726808, 12.35526082,
            12.36325873, 12.37126182, 12.37927009, 12.38728355, 12.39530219,
            12.40332602, 12.41135505, 12.41938928, 12.4274287 , 12.43547333,
            12.44352317, 12.45157822, 12.45963848, 12.46770396, 12.47577466,
            12.48385059, 12.49193174, 12.50001813, 12.50810974, 12.5162066 ,
            12.5243087 , 12.53241604, 12.54052863, 12.54864648, 12.55676957,
            12.56489793, 12.57303155, 12.58117043, 12.58931458, 12.59746401,
            12.6056187 , 12.61377868, 12.62194394, 12.63011449, 12.63829032,
            12.64647145, 12.65465787, 12.66284959, 12.67104662, 12.67924895,
            12.68745659, 12.69566954, 12.70388781, 12.7121114 , 12.72034031,
            12.72857455, 12.73681412, 12.74505903, 12.75330927, 12.76156485,
            12.76982578, 12.77809205, 12.78636367, 12.79464065, 12.80292299,
            12.81121069, 12.81950375, 12.82780218, 12.83610598, 12.84441516,
            12.85272972, 12.86104966, 12.86937498, 12.8777057 , 12.8860418 ,
            12.89438331, 12.90273021, 12.91108252, 12.91944023, 12.92780335,
            12.93617189, 12.94454584, 12.95292522, 12.96131002, 12.96970024,
            12.9780959 , 12.98649699, 12.99490352, 13.0033155 , 13.01173291,
            13.02015578, 13.0285841 , 13.03701788, 13.04545711, 13.05390181,
            13.06235197, 13.0708076 , 13.07926871, 13.0877353 , 13.09620736,
            13.10468491, 13.11316795, 13.12165648, 13.1301505 , 13.13865002,
            13.14715505, 13.15566558, 13.16418161, 13.17270316, 13.18123023,
            13.18976282, 13.19830093, 13.20684457, 13.21539374, 13.22394844,
            13.23250868, 13.24107446, 13.24964578, 13.25822266, 13.26680509,
            13.27539307, 13.28398661, 13.29258571, 13.30119038, 13.30980063,
            13.31841644, 13.32703783, 13.3356648 , 13.34429736, 13.35293551,
            13.36157924, 13.37022858, 13.37888351, 13.38754404, 13.39621018,
            13.40488193, 13.41355929, 13.42224227, 13.43093087, 13.4396251 ,
            13.44832495, 13.45703044, 13.46574156, 13.47445832, 13.48318072,
            13.49190877, 13.50064247, 13.50938182, 13.51812683, 13.5268775 ,
            13.53563383, 13.54439584, 13.55316351, 13.56193686, 13.57071589,
            13.5795006 , 13.588291  , 13.59708709, 13.60588887, 13.61469635,
            13.62350954, 13.63232842, 13.64115302, 13.64998333, 13.65881935,
            13.6676611 , 13.67650856, 13.68536176, 13.69422069, 13.70308535,
            13.71195574, 13.72083189, 13.72971377, 13.73860141, 13.7474948 ,
            13.75639394, 13.76529885, 13.77420952, 13.78312596, 13.79204817,
            13.80097616, 13.80990993, 13.81884948, 13.82779481, 13.83674594,
            13.84570286, 13.85466558, 13.8636341 , 13.87260843, 13.88158856,
            13.89057451, 13.89956628, 13.90856387, 13.91756728, 13.92657652,
            13.93559159, 13.94461249, 13.95363924, 13.96267183, 13.97171027,
            13.98075455, 13.9898047 , 13.9988607 , 14.00792256, 14.01699029,
            14.02606389, 14.03514336, 14.04422871, 14.05331994, 14.06241706,
            14.07152006, 14.08062896, 14.08974375, 14.09886444, 14.10799104,
            14.11712355, 14.12626197, 14.1354063 , 14.14455655, 14.15371273,
            14.16287483, 14.17204286, 14.18121683, 14.19039674, 14.19958259,
            14.20877439, 14.21797213, 14.22717583, 14.23638549, 14.24560111,
            14.25482269, 14.26405025, 14.27328377, 14.28252328, 14.29176876,
            14.30102024, 14.31027769, 14.31954115, 14.32881059, 14.33808604,
            14.3473675 , 14.35665496, 14.36594843, 14.37524792, 14.38455343,
            14.39386496, 14.40318252, 14.41250611, 14.42183574, 14.43117141,
            14.44051312, 14.44986087, 14.45921468, 14.46857455, 14.47794047,
            14.48731245, 14.4966905 , 14.50607463, 14.51546482, 14.5248611 ,
            14.53426346, 14.5436719 , 14.55308643, 14.56250706, 14.57193379,
            14.58136662, 14.59080556, 14.6002506 , 14.60970176, 14.61915904,
            14.62862244, 14.63809196, 14.64756762, 14.65704941, 14.66653733,
            14.6760314 , 14.68553162, 14.69503798, 14.7045505 , 14.71406918,
            14.72359401, 14.73312502, 14.74266219, 14.75220554, 14.76175506,
            14.77131077, 14.78087266, 14.79044074, 14.80001502, 14.80959549,
            14.81918216, 14.82877504, 14.83837413, 14.84797944, 14.85759096,
            14.8672087 , 14.87683267, 14.88646287, 14.8960993 , 14.90574197,
            14.91539089, 14.92504605, 14.93470746, 14.94437512, 14.95404904,
            14.96372922, 14.97341567, 14.98310839, 14.99280739, 15.00251266,
            15.01222422, 15.02194206, 15.03166619, 15.04139662, 15.05113334,
            15.06087637, 15.07062571, 15.08038136, 15.09014332, 15.0999116 ,
            15.1096862 , 15.11946713, 15.1292544 , 15.139048  , 15.14884794,
            15.15865422, 15.16846685, 15.17828583, 15.18811117, 15.19794287,
            15.20778093, 15.21762536, 15.22747617, 15.23733335, 15.24719691,
            15.25706685, 15.26694319, 15.27682592, 15.28671504, 15.29661057,
            15.30651251, 15.31642085, 15.32633561, 15.33625678, 15.34618438,
            15.3561184 , 15.36605886, 15.37600575, 15.38595907, 15.39591884,
            15.40588506, 15.41585773, 15.42583686, 15.43582244, 15.44581449,
            15.45581301, 15.465818  , 15.47582947, 15.48584741, 15.49587184,
            15.50590277, 15.51594018, 15.52598409, 15.5360345 , 15.54609142,
            15.55615485, 15.5662248 , 15.57630126, 15.58638424, 15.59647376,
            15.6065698 , 15.61667238, 15.6267815 , 15.63689716, 15.64701937,
            15.65714813, 15.66728345, 15.67742533, 15.68757378, 15.69772879,
            15.70789038, 15.71805855, 15.7282333 , 15.73841463, 15.74860256,
            15.75879708, 15.7689982 , 15.77920592, 15.78942025, 15.7996412 ,
            15.80986876, 15.82010294, 15.83034374, 15.84059117, 15.85084524,
            15.86110595, 15.87137329, 15.88164729, 15.89192793, 15.90221523,
            15.91250919, 15.92280981, 15.9331171 , 15.94343106, 15.9537517 ,
            15.96407902, 15.97441303, 15.98475372, 15.99510111, 16.0054552 ,
            16.01581598, 16.02618348, 16.03655769, 16.04693861, 16.05732625,
            16.06772062, 16.07812171, 16.08852954, 16.09894411, 16.10936541,
            16.11979347, 16.13022827, 16.14066983, 16.15111814, 16.16157322,
            16.17203507, 16.18250369, 16.19297909, 16.20346127, 16.21395023,
            16.22444599, 16.23494853, 16.24545788, 16.25597403, 16.26649699,
            16.27702675, 16.28756334, 16.29810674, 16.30865697, 16.31921403,
            16.32977793, 16.34034866, 16.35092624, 16.36151066, 16.37210193,
            16.38270006, 16.39330505, 16.40391691, 16.41453563, 16.42516123,
            16.4357937 , 16.44643306, 16.45707931, 16.46773245, 16.47839248,
            16.48905942, 16.49973326, 16.510414  , 16.52110167, 16.53179625,
            16.54249775, 16.55320619, 16.56392155, 16.57464385, 16.58537309,
            16.59610928, 16.60685241, 16.6176025 , 16.62835955, 16.63912356,
            16.64989454, 16.6606725 , 16.67145743, 16.68224934, 16.69304823,
            16.70385412, 16.714667  , 16.72548689, 16.73631377, 16.74714767,
            16.75798857, 16.7688365 , 16.77969145, 16.79055342, 16.80142242,
            16.81229847, 16.82318155, 16.83407167, 16.84496885, 16.85587308,
            16.86678437, 16.87770272, 16.88862814, 16.89956063, 16.9105002 ,
            16.92144685, 16.93240059, 16.94336141, 16.95432934, 16.96530436,
            16.97628648, 16.98727572, 16.99827207, 17.00927554, 17.02028613,
            17.03130384, 17.04232869, 17.05336068, 17.06439981, 17.07544608,
            17.08649951, 17.09756009, 17.10862783, 17.11970273, 17.1307848 ,
            17.14187405, 17.15297047, 17.16407408, 17.17518488, 17.18630287,
            17.19742805, 17.20856044, 17.21970003, 17.23084684, 17.24200086,
            17.2531621 , 17.26433056, 17.27550626, 17.28668918, 17.29787935,
            17.30907676, 17.32028142, 17.33149334, 17.34271251, 17.35393894,
            17.36517264, 17.37641362, 17.38766187, 17.3989174 , 17.41018021,
            17.42145032, 17.43272772, 17.44401243, 17.45530443, 17.46660375,
            17.47791038, 17.48922433, 17.50054561, 17.51187421, 17.52321015,
            17.53455342, 17.54590404, 17.55726201, 17.56862733, 17.58,   
        ]
    )
    assert np.allclose(
        y_fit,
        [
            -1.20092802e+00, -1.19910015e+00, -1.19724944e+00, -1.19537562e+00,
            -1.19347839e+00, -1.19155745e+00, -1.18961252e+00, -1.18764329e+00,
            -1.18564947e+00, -1.18363074e+00, -1.18158680e+00, -1.17951733e+00,
            -1.17742201e+00, -1.17530053e+00, -1.17315255e+00, -1.17097776e+00,
            -1.16877580e+00, -1.16654635e+00, -1.16428907e+00, -1.16200360e+00,
            -1.15968960e+00, -1.15734671e+00, -1.15497457e+00, -1.15257282e+00,
            -1.15014110e+00, -1.14767902e+00, -1.14518621e+00, -1.14266229e+00,
            -1.14010687e+00, -1.13751956e+00, -1.13489997e+00, -1.13224769e+00,
            -1.12956231e+00, -1.12684343e+00, -1.12409063e+00, -1.12130349e+00,
            -1.11848158e+00, -1.11562447e+00, -1.11273172e+00, -1.10980290e+00,
            -1.10683754e+00, -1.10383521e+00, -1.10079543e+00, -1.09771775e+00,
            -1.09460169e+00, -1.09144679e+00, -1.08825255e+00, -1.08501849e+00,
            -1.08174411e+00, -1.07842892e+00, -1.07507241e+00, -1.07167407e+00,
            -1.06823337e+00, -1.06474980e+00, -1.06122282e+00, -1.05765190e+00,
            -1.05403649e+00, -1.05037603e+00, -1.04666998e+00, -1.04291776e+00,
            -1.03911881e+00, -1.03527255e+00, -1.03137838e+00, -1.02743573e+00,
            -1.02344398e+00, -1.01940253e+00, -1.01531077e+00, -1.01116808e+00,
            -1.00697382e+00, -1.00272735e+00, -9.98428036e-01, -9.94075220e-01,
            -9.89668240e-01, -9.85206429e-01, -9.80689108e-01, -9.76115592e-01,
            -9.71485186e-01, -9.66797190e-01, -9.62050891e-01, -9.57245571e-01,
            -9.52380500e-01, -9.47454942e-01, -9.42468152e-01, -9.37419373e-01,
            -9.32307841e-01, -9.27132784e-01, -9.21893417e-01, -9.16588950e-01,
            -9.11218578e-01, -9.05781493e-01, -9.00276870e-01, -8.94703880e-01,
            -8.89061680e-01, -8.83349420e-01, -8.77566236e-01, -8.71711257e-01,
            -8.65783601e-01, -8.59782372e-01, -8.53706668e-01, -8.47555573e-01,
            -8.41328161e-01, -8.35023494e-01, -8.28640625e-01, -8.22178592e-01,
            -8.15636425e-01, -8.09013140e-01, -8.02307743e-01, -7.95519226e-01,
            -7.88646570e-01, -7.81688745e-01, -7.74644706e-01, -7.67513398e-01,
            -7.60293753e-01, -7.52984688e-01, -7.45585109e-01, -7.38093909e-01,
            -7.30509968e-01, -7.22832151e-01, -7.15059311e-01, -7.07190287e-01,
            -6.99223903e-01, -6.91158971e-01, -6.82994289e-01, -6.74728638e-01,
            -6.66360786e-01, -6.57889488e-01, -6.49313482e-01, -6.40631493e-01,
            -6.31842228e-01, -6.22944382e-01, -6.13936632e-01, -6.04817642e-01,
            -5.95586058e-01, -5.86240510e-01, -5.76779614e-01, -5.67201967e-01,
            -5.57506152e-01, -5.47690734e-01, -5.37754262e-01, -5.27695266e-01,
            -5.17512260e-01, -5.07203743e-01, -4.96768192e-01, -4.86204069e-01,
            -4.75509818e-01, -4.64683864e-01, -4.53724613e-01, -4.42630455e-01,
            -4.31399759e-01, -4.20030875e-01, -4.08522136e-01, -3.96871853e-01,
            -3.85078318e-01, -3.73139806e-01, -3.61054569e-01, -3.48820839e-01,
            -3.36436829e-01, -3.23900731e-01, -3.11210716e-01, -2.98364933e-01,
            -2.85361512e-01, -2.72198559e-01, -2.58874160e-01, -2.45386379e-01,
            -2.31733257e-01, -2.17912814e-01, -2.03923045e-01, -1.89761925e-01,
            -1.75427404e-01, -1.60917410e-01, -1.46229846e-01, -1.31362594e-01,
            -1.16313508e-01, -1.01080420e-01, -8.56611396e-02, -7.00534479e-02,
            -5.42551032e-02, -3.82638382e-02, -2.20773600e-02, -5.69335024e-03,
            1.08905355e-02,  2.76766677e-02,  4.46674435e-02,  6.18652864e-02,
            7.92726471e-02,  9.68920033e-02,  1.14725860e-01,  1.32776751e-01,
            1.51047236e-01,  1.69539906e-01,  1.88257376e-01,  2.07202294e-01,
            2.26377335e-01,  2.45785204e-01,  2.65428635e-01,  2.85310392e-01,
            3.05433268e-01,  3.25800089e-01,  3.46413709e-01,  3.67277014e-01,
            3.88392921e-01,  4.09764379e-01,  4.31394367e-01,  4.53285898e-01,
            4.75442016e-01,  4.97865798e-01,  5.20560354e-01,  5.43528825e-01,
            5.66774389e-01,  5.90300255e-01,  6.14109666e-01,  6.38205900e-01,
            6.62592269e-01,  6.87272119e-01,  7.12248834e-01,  7.37525829e-01,
            7.63106557e-01,  7.88994507e-01,  8.15193203e-01,  8.41706205e-01,
            8.68537112e-01,  8.95689558e-01,  9.23167214e-01,  9.50973789e-01,
            9.79113030e-01,  1.00758872e+00,  1.03640469e+00,  1.06556478e+00,
            1.09507292e+00,  1.12493303e+00,  1.15514909e+00,  1.18572512e+00,
            1.21666518e+00,  1.24797337e+00,  1.27965382e+00,  1.31171072e+00,
            1.34414828e+00,  1.37697077e+00,  1.41018248e+00,  1.44378776e+00,
            1.47779100e+00,  1.51219662e+00,  1.54700910e+00,  1.58223294e+00,
            1.61787271e+00,  1.65393299e+00,  1.69041844e+00,  1.72733373e+00,
            1.76468359e+00,  1.80247280e+00,  1.84070616e+00,  1.87938856e+00,
            1.91852487e+00,  1.95812007e+00,  1.99817913e+00,  2.03870710e+00,
            2.07970906e+00,  2.12119014e+00,  2.16315552e+00,  2.20561041e+00,
            2.24856009e+00,  2.29200986e+00,  2.33596508e+00,  2.38043115e+00,
            2.42541353e+00,  2.47091772e+00,  2.51694924e+00,  2.56351370e+00,
            2.61061672e+00,  2.65826400e+00,  2.70646126e+00,  2.75521427e+00,
            2.80452886e+00,  2.85441090e+00,  2.90486630e+00,  2.95590103e+00,
            3.00752109e+00,  3.05973255e+00,  3.11254151e+00,  3.16595411e+00,
            3.21997656e+00,  3.27461510e+00,  3.32987602e+00,  3.38576566e+00,
            3.44229039e+00,  3.49945665e+00,  3.55727092e+00,  3.61573972e+00,
            3.67486961e+00,  3.73466721e+00,  3.79513918e+00,  3.85629222e+00,
            3.91813308e+00,  3.98066856e+00,  4.04390549e+00,  4.10785075e+00,
            4.17251128e+00,  4.23789405e+00,  4.30400606e+00,  4.37085438e+00,
            4.43844610e+00,  4.50678837e+00,  4.57588837e+00,  4.64575332e+00,
            4.71639050e+00,  4.78780720e+00,  4.86001078e+00,  4.93300862e+00,
            5.00680814e+00,  5.08141681e+00,  5.15684212e+00,  5.23309162e+00,
            5.31017289e+00,  5.38809352e+00,  5.46686116e+00,  5.54648350e+00,
            5.62696825e+00,  5.70832314e+00,  5.79055597e+00,  5.87367453e+00,
            5.95768668e+00,  6.04260027e+00,  6.12842320e+00,  6.21516340e+00,
            6.30282882e+00,  6.39142744e+00,  6.48096725e+00,  6.57145628e+00,
            6.66290258e+00,  6.75531422e+00,  6.84869928e+00,  6.94306587e+00,
            7.03842212e+00,  7.13477616e+00,  7.23213615e+00,  7.33051026e+00,
            7.42990667e+00,  7.53033357e+00,  7.63179917e+00,  7.73431167e+00,
            7.83787928e+00,  7.94251023e+00,  8.04821274e+00,  8.15499504e+00,
            8.26286534e+00,  8.37183188e+00,  8.48190286e+00,  8.59308650e+00,
            8.70539101e+00,  8.81882458e+00,  8.93339540e+00,  9.04911164e+00,
            9.16598146e+00,  9.28401299e+00,  9.40321435e+00,  9.52359365e+00,
            9.64515896e+00,  9.76791832e+00,  9.89187977e+00,  1.00170513e+01,
            1.01434408e+01,  1.02710563e+01,  1.03999056e+01,  1.05299966e+01,
            1.06613371e+01,  1.07939349e+01,  1.09277976e+01,  1.10629329e+01,
            1.11993484e+01,  1.13370517e+01,  1.14760502e+01,  1.16163515e+01,
            1.17579628e+01,  1.19008915e+01,  1.20451448e+01,  1.21907298e+01,
            1.23376537e+01,  1.24859235e+01,  1.26355460e+01,  1.27865281e+01,
            1.29388766e+01,  1.30925981e+01,  1.32476992e+01,  1.34041863e+01,
            1.35620659e+01,  1.37213441e+01,  1.38820272e+01,  1.40441212e+01,
            1.42076319e+01,  1.43725654e+01,  1.45389271e+01,  1.47067227e+01,
            1.48759577e+01,  1.50466373e+01,  1.52187667e+01,  1.53923510e+01,
            1.55673950e+01,  1.57439035e+01,  1.59218811e+01,  1.61013323e+01,
            1.62822613e+01,  1.64646722e+01,  1.66485691e+01,  1.68339556e+01,
            1.70208356e+01,  1.72092123e+01,  1.73990891e+01,  1.75904691e+01,
            1.77833551e+01,  1.79777500e+01,  1.81736562e+01,  1.83710760e+01,
            1.85700116e+01,  1.87704648e+01,  1.89724375e+01,  1.91759311e+01,
            1.93809469e+01,  1.95874860e+01,  1.97955492e+01,  2.00051371e+01,
            2.02162502e+01,  2.04288886e+01,  2.06430522e+01,  2.08587407e+01,
            2.10759535e+01,  2.12946900e+01,  2.15149489e+01,  2.17367290e+01,
            2.19600287e+01,  2.21848463e+01,  2.24111796e+01,  2.26390263e+01,
            2.28683838e+01,  2.30992492e+01,  2.33316193e+01,  2.35654908e+01,
            2.38008598e+01,  2.40377225e+01,  2.42760744e+01,  2.45159112e+01,
            2.47572279e+01,  2.50000193e+01,  2.52442801e+01,  2.54900045e+01,
            2.57371865e+01,  2.59858197e+01,  2.62358976e+01,  2.64874131e+01,
            2.67403591e+01,  2.69947281e+01,  2.72505121e+01,  2.75077030e+01,
            2.77662924e+01,  2.80262715e+01,  2.82876312e+01,  2.85503620e+01,
            2.88144544e+01,  2.90798982e+01,  2.93466832e+01,  2.96147986e+01,
            2.98842335e+01,  3.01549767e+01,  3.04270165e+01,  3.07003411e+01,
            3.09749381e+01,  3.12507952e+01,  3.15278994e+01,  3.18062376e+01,
            3.20857963e+01,  3.23665618e+01,  3.26485200e+01,  3.29316565e+01,
            3.32159566e+01,  3.35014053e+01,  3.37879873e+01,  3.40756871e+01,
            3.43644888e+01,  3.46543761e+01,  3.49453327e+01,  3.52373417e+01,
            3.55303862e+01,  3.58244488e+01,  3.61195118e+01,  3.64155575e+01,
            3.67125677e+01,  3.70105239e+01,  3.73094075e+01,  3.76091995e+01,
            3.79098807e+01,  3.82114317e+01,  3.85138328e+01,  3.88170641e+01,
            3.91211052e+01,  3.94259359e+01,  3.97315355e+01,  4.00378831e+01,
            4.03449577e+01,  4.06527379e+01,  4.09612021e+01,  4.12703288e+01,
            4.15800961e+01,  4.18904817e+01,  4.22014634e+01,  4.25130188e+01,
            4.28251252e+01,  4.31377599e+01,  4.34508999e+01,  4.37645220e+01,
            4.40786030e+01,  4.43931196e+01,  4.47080481e+01,  4.50233650e+01,
            4.53390465e+01,  4.56550686e+01,  4.59714074e+01,  4.62880388e+01,
            4.66049387e+01,  4.69220828e+01,  4.72394466e+01,  4.75570060e+01,
            4.78747363e+01,  4.81926130e+01,  4.85106117e+01,  4.88287077e+01,
            4.91468764e+01,  4.94650931e+01,  4.97833332e+01,  5.01015719e+01,
            5.04197847e+01,  5.07379468e+01,  5.10560337e+01,  5.13740206e+01,
            5.16918831e+01,  5.20095965e+01,  5.23271363e+01,  5.26444780e+01,
            5.29615974e+01,  5.32784700e+01,  5.35950716e+01,  5.39113780e+01,
            5.42273653e+01,  5.45430093e+01,  5.48582862e+01,  5.51731722e+01,
            5.54876438e+01,  5.58016774e+01,  5.61152496e+01,  5.64283371e+01,
            5.67409170e+01,  5.70529662e+01,  5.73644620e+01,  5.76753817e+01,
            5.79857029e+01,  5.82954034e+01,  5.86044610e+01,  5.89128539e+01,
            5.92205604e+01,  5.95275591e+01,  5.98338285e+01,  6.01393477e+01,
            6.04440958e+01,  6.07480523e+01,  6.10511966e+01,  6.13535087e+01,
            6.16549686e+01,  6.19555566e+01,  6.22552534e+01,  6.25540397e+01,
            6.28518967e+01,  6.31488057e+01,  6.34447482e+01,  6.37397063e+01,
            6.40336619e+01,  6.43265976e+01,  6.46184961e+01,  6.49093403e+01,
            6.51991135e+01,  6.54877993e+01,  6.57753816e+01,  6.60618445e+01,
            6.63471723e+01,  6.66313500e+01,  6.69143625e+01,  6.71961951e+01,
            6.74768335e+01,  6.77562638e+01,  6.80344720e+01,  6.83114448e+01,
            6.85871692e+01,  6.88616322e+01,  6.91348213e+01,  6.94067245e+01,
            6.96773298e+01,  6.99466256e+01,  7.02146007e+01,  7.04812443e+01,
            7.07465456e+01,  7.10104943e+01,  7.12730805e+01,  7.15342945e+01,
            7.17941270e+01,  7.20525688e+01,  7.23096112e+01,  7.25652459e+01,
            7.28194646e+01,  7.30722596e+01,  7.33236234e+01,  7.35735487e+01,
            7.38220286e+01,  7.40690566e+01,  7.43146264e+01,  7.45587320e+01,
            7.48013676e+01,  7.50425279e+01,  7.52822078e+01,  7.55204024e+01,
            7.57571072e+01,  7.59923179e+01,  7.62260306e+01,  7.64582417e+01,
            7.66889476e+01,  7.69181454e+01,  7.71458321e+01,  7.73720051e+01,
            7.75966621e+01,  7.78198011e+01,  7.80414203e+01,  7.82615182e+01,
            7.84800934e+01,  7.86971450e+01,  7.89126722e+01,  7.91266744e+01,
            7.93391513e+01,  7.95501030e+01,  7.97595295e+01,  7.99674314e+01,
            8.01738093e+01,  8.03786639e+01,  8.05819965e+01,  8.07838083e+01,
            8.09841009e+01,  8.11828760e+01,  8.13801355e+01,  8.15758816e+01,
            8.17701167e+01,  8.19628433e+01,  8.21540640e+01,  8.23437819e+01,
            8.25320001e+01,  8.27187219e+01,  8.29039506e+01,  8.30876900e+01,
            8.32699440e+01,  8.34507163e+01,  8.36300113e+01,  8.38078333e+01,
            8.39841866e+01,  8.41590759e+01,  8.43325060e+01,  8.45044817e+01,
            8.46750082e+01,  8.48440906e+01,  8.50117343e+01,  8.51779446e+01,
            8.53427272e+01,  8.55060878e+01,  8.56680321e+01,  8.58285663e+01,
            8.59876962e+01,  8.61454281e+01,  8.63017683e+01,  8.64567231e+01,
            8.66102990e+01,  8.67625025e+01,  8.69133404e+01,  8.70628195e+01,
            8.72109465e+01,  8.73577283e+01,  8.75031721e+01,  8.76472849e+01,
            8.77900738e+01,  8.79315462e+01,  8.80717092e+01,  8.82105704e+01,
            8.83481370e+01,  8.84844167e+01,  8.86194170e+01,  8.87531454e+01,
            8.88856097e+01,  8.90168176e+01,  8.91467769e+01,  8.92754953e+01,
            8.94029807e+01,  8.95292409e+01,  8.96542840e+01,  8.97781179e+01,
            8.99007505e+01,  9.00221899e+01,  9.01424442e+01,  9.02615214e+01,
            9.03794296e+01,  9.04961769e+01,  9.06117716e+01,  9.07262216e+01,
            9.08395353e+01,  9.09517209e+01,  9.10627864e+01,  9.11727401e+01,
            9.12815902e+01,  9.13893450e+01,  9.14960126e+01,  9.16016014e+01,
            9.17061194e+01,  9.18095750e+01,  9.19119763e+01,  9.20133316e+01,
            9.21136490e+01,  9.22129369e+01,  9.23112033e+01,  9.24084564e+01,
            9.25047045e+01,  9.25999556e+01,  9.26942180e+01,  9.27874996e+01,
            9.28798087e+01,  9.29711534e+01,  9.30615416e+01,  9.31509814e+01,
            9.32394809e+01,  9.33270480e+01,  9.34136908e+01,  9.34994171e+01,
            9.35842349e+01,  9.36681521e+01,  9.37511766e+01,  9.38333161e+01,
            9.39145786e+01,  9.39949717e+01,  9.40745032e+01,  9.41531809e+01,
            9.42310123e+01,  9.43080052e+01,  9.43841671e+01,  9.44595057e+01,
            9.45340284e+01,  9.46077427e+01,  9.46806561e+01,  9.47527761e+01,
            9.48241099e+01,  9.48946651e+01,  9.49644487e+01,  9.50334682e+01,
            9.51017307e+01,  9.51692434e+01,  9.52360135e+01,  9.53020480e+01,
            9.53673540e+01,  9.54319385e+01,  9.54958085e+01,  9.55589708e+01,
            9.56214325e+01,  9.56832002e+01,  9.57442809e+01,  9.58046812e+01,
            9.58644078e+01,  9.59234674e+01,  9.59818666e+01,  9.60396120e+01,
            9.60967101e+01,  9.61531673e+01,  9.62089901e+01,  9.62641849e+01,
            9.63187579e+01,  9.63727156e+01,  9.64260640e+01,  9.64788094e+01,
            9.65309580e+01,  9.65825158e+01,  9.66334890e+01,  9.66838834e+01,
            9.67337051e+01,  9.67829600e+01,  9.68316539e+01,  9.68797927e+01,
            9.69273821e+01,  9.69744279e+01,  9.70209357e+01,  9.70669112e+01,
            9.71123599e+01,  9.71572873e+01,  9.72016991e+01,  9.72456006e+01,
            9.72889972e+01,  9.73318942e+01,  9.73742971e+01,  9.74162110e+01,
            9.74576411e+01,  9.74985927e+01,  9.75390708e+01,  9.75790805e+01,
            9.76186269e+01,  9.76577149e+01,  9.76963496e+01,  9.77345357e+01,
            9.77722782e+01,  9.78095819e+01,  9.78464514e+01,  9.78828917e+01,
            9.79189072e+01,  9.79545028e+01,  9.79896829e+01,  9.80244521e+01,
            9.80588149e+01,  9.80927758e+01,  9.81263393e+01,  9.81595096e+01,
            9.81922911e+01,  9.82246882e+01,  9.82567051e+01,  9.82883459e+01,
            9.83196150e+01,  9.83505163e+01,  9.83810540e+01,  9.84112323e+01,
            9.84410549e+01,  9.84705260e+01,  9.84996495e+01,  9.85284293e+01,
            9.85568692e+01,  9.85849731e+01,  9.86127447e+01,  9.86401877e+01,
            9.86673060e+01,  9.86941031e+01,  9.87205826e+01,  9.87467483e+01,
            9.87726036e+01,  9.87981520e+01,  9.88233970e+01,  9.88483422e+01,
            9.88729908e+01,  9.88973463e+01,  9.89214120e+01,  9.89451913e+01,
            9.89686873e+01,  9.89919034e+01,  9.90148428e+01,  9.90375085e+01,
            9.90599038e+01,  9.90820318e+01,  9.91038955e+01,  9.91254980e+01,
            9.91468423e+01,  9.91679313e+01,  9.91887681e+01,  9.92093554e+01,
            9.92296963e+01,  9.92497935e+01,  9.92696499e+01,  9.92892683e+01,
            9.93086514e+01,  9.93278020e+01,  9.93467227e+01,  9.93654162e+01,
            9.93838853e+01,  9.94021324e+01,  9.94201602e+01,  9.94379712e+01,
            9.94555681e+01,  9.94729531e+01,  9.94901289e+01,  9.95070979e+01,
            9.95238626e+01,  9.95404252e+01,  9.95567882e+01,  9.95729539e+01,
            9.95889246e+01,  9.96047027e+01,  9.96202903e+01,  9.96356898e+01,
            9.96509033e+01,  9.96659331e+01,  9.96807812e+01,  9.96954499e+01,
            9.97099412e+01,  9.97242573e+01,  9.97384002e+01,  9.97523719e+01,
            9.97661746e+01,  9.97798101e+01,  9.97932805e+01,  9.98065877e+01,
            9.98197337e+01,  9.98327203e+01,  9.98455496e+01,  9.98582232e+01,
            9.98707431e+01,  9.98831111e+01,  9.98953291e+01,  9.99073987e+01,
            9.99193218e+01,  9.99311001e+01,  9.99427353e+01,  9.99542292e+01,
            9.99655833e+01,  9.99767995e+01,  9.99878793e+01,  9.99988244e+01,
            1.00009636e+02,  1.00020317e+02,  1.00030867e+02,  1.00041289e+02,
            1.00051584e+02,  1.00061754e+02,  1.00071800e+02,  1.00081724e+02,
            1.00091526e+02,  1.00101210e+02,  1.00110775e+02,  1.00120224e+02,
            1.00129557e+02,  1.00138777e+02,  1.00147884e+02,  1.00156880e+02,
            1.00165766e+02,  1.00174544e+02,  1.00183215e+02,  1.00191779e+02,
            1.00200240e+02,  1.00208597e+02,  1.00216852e+02,  1.00225006e+02,
            1.00233060e+02,  1.00241016e+02,  1.00248875e+02,  1.00256638e+02,
            1.00264306e+02,  1.00271880e+02,  1.00279361e+02,  1.00286751e+02,
            1.00294051e+02,  1.00301261e+02,  1.00308383e+02,  1.00315418e+02,
            1.00322366e+02,  1.00329230e+02,  1.00336010e+02,  1.00342707e+02,
            1.00349321e+02,  1.00355855e+02,  1.00362308e+02,  1.00368683e+02,
            1.00374979e+02,  1.00381199e+02,  1.00387342e+02,  1.00393410e+02,
            1.00399403e+02,  1.00405323e+02,  1.00411170e+02,  1.00416946e+02,
            1.00422651e+02,  1.00428285e+02,  1.00433851e+02,  1.00439349e+02,
            1.00444779e+02,  1.00450142e+02,  1.00455440e+02,  1.00460672e+02,
            1.00465840e+02,  1.00470945e+02,  1.00475987e+02,  1.00480968e+02,
            1.00485887e+02,  1.00490746e+02,  1.00495545e+02,  1.00500285e+02,
            1.00504967e+02,  1.00509591e+02,  1.00514158e+02,  1.00518670e+02,
            1.00523126e+02,  1.00527527e+02,  1.00531874e+02,  1.00536168e+02,
            1.00540409e+02,  1.00544598e+02,  1.00548735e+02,  1.00552821e+02,
            1.00556857e+02,  1.00560844e+02,  1.00564781e+02,  1.00568670e+02,
            1.00572512e+02,  1.00576306e+02,  1.00580053e+02,  1.00583754e+02,
            1.00587410e+02,  1.00591020e+02,  1.00594587e+02,  1.00598109e+02,
        ]
    )
