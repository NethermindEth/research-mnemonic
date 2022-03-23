def get_primitive_poly(degree):
    """!Returns, in string form, a primitive polynomial over GF(2) of degree between 9 and 660.
    
    These primitive polynomials have been obtained from the following paper:

    Rajski, J., & Tyszer, J. (2003). Primitive polynomials over GF(2) of degree up to 660 with 
    uniformly distributed coefficients. Journal of Electronic Testing, 19(6), 645-657.
    """

    assert 9<=degree and degree<=660, 'Only primitive polynomials of degrees between 9 and 660 are available, but degree ' + str(degree) + ' was requested.'
    return polynomials[str(degree)]

polynomials = {
    "9": "x^9 + x^7 + x^5 + x^2 + 1",
    "10": "x^10 + x^8 + x^5 + x^4 + 1",
    "11": "x^11 + x^9 + x^6 + x^3 + 1",
    "12": "x^12 + x^9 + x^8 + x^5 + 1",
    "13": "x^13 + x^10 + x^6 + x^4 + 1",
    "14": "x^14 + x^12 + x^7 + x^5 + 1",
    "15": "x^15 + x^12 + x^9 + x^4 + 1",
    "16": "x^16 + x^12 + x^9 + x^6 + 1",
    "17": "x^17 + x^13 + x^9 + x^5 + 1",
    "18": "x^18 + x^14 + x^9 + x^3 + 1",
    "19": "x^19 + x^15 + x^10 + x^6 + 1",
    "20": "x^20 + x^15 + x^11 + x^7 + 1",
    "21": "x^21 + x^16 + x^10 + x^4 + 1",
    "22": "x^22 + x^17 + x^10 + x^6 + 1",
    "23": "x^23 + x^18 + x^12 + x^6 + 1",
    "24": "x^24 + x^19 + x^13 + x^4 + 1",
    "25": "x^25 + x^19 + x^13 + x^7 + 1",
    "26": "x^26 + x^20 + x^13 + x^9 + 1",
    "27": "x^27 + x^20 + x^14 + x^7 + 1",
    "28": "x^28 + x^21 + x^13 + x^7 + 1",
    "29": "x^29 + x^21 + x^15 + x^9 + 1",
    "30": "x^30 + x^22 + x^17 + x^10 + 1",
    "31": "x^31 + x^24 + x^16 + x^8 + 1",
    "32": "x^32 + x^25 + x^17 + x^7 + 1",
    "33": "x^33 + x^25 + x^17 + x^8 + 1",
    "34": "x^34 + x^27 + x^19 + x^10 + 1",
    "35": "x^35 + x^27 + x^18 + x^8 + 1",
    "36": "x^36 + x^28 + x^19 + x^11 + 1",
    "37": "x^37 + x^28 + x^19 + x^9 + 1",
    "38": "x^38 + x^29 + x^18 + x^10 + 1",
    "39": "x^39 + x^30 + x^21 + x^11 + 1",
    "40": "x^40 + x^30 + x^19 + x^11 + 1",
    "41": "x^41 + x^31 + x^22 + x^12 + 1",
    "42": "x^42 + x^32 + x^23 + x^11 + 1",
    "43": "x^43 + x^33 + x^22 + x^10 + 1",
    "44": "x^44 + x^33 + x^22 + x^13 + 1",
    "45": "x^45 + x^35 + x^23 + x^13 + 1",
    "46": "x^46 + x^36 + x^23 + x^13 + 1",
    "47": "x^47 + x^36 + x^23 + x^12 + 1",
    "48": "x^48 + x^35 + x^22 + x^10 + 1",
    "49": "x^49 + x^37 + x^26 + x^14 + 1",
    "50": "x^50 + x^38 + x^26 + x^11 + 1",
    "51": "x^51 + x^39 + x^26 + x^12 + 1",
    "52": "x^52 + x^40 + x^27 + x^15 + 1",
    "53": "x^53 + x^38 + x^24 + x^11 + 1",
    "54": "x^54 + x^41 + x^27 + x^14 + 1",
    "55": "x^55 + x^42 + x^29 + x^14 + 1",
    "56": "x^56 + x^43 + x^25 + x^12 + 1",
    "57": "x^57 + x^43 + x^28 + x^13 + 1",
    "58": "x^58 + x^44 + x^28 + x^15 + 1",
    "59": "x^59 + x^45 + x^29 + x^15 + 1",
    "60": "x^60 + x^44 + x^29 + x^16 + 1",
    "61": "x^61 + x^46 + x^30 + x^13 + 1",
    "62": "x^62 + x^45 + x^30 + x^18 + 1",
    "63": "x^63 + x^49 + x^34 + x^17 + 1",
    "64": "x^64 + x^50 + x^33 + x^19 + 1",
    "65": "x^65 + x^50 + x^32 + x^18 + 1",
    "66": "x^66 + x^50 + x^33 + x^18 + 1",
    "67": "x^67 + x^49 + x^32 + x^18 + 1",
    "68": "x^68 + x^51 + x^35 + x^19 + 1",
    "69": "x^69 + x^52 + x^35 + x^17 + 1",
    "70": "x^70 + x^53 + x^35 + x^18 + 1",
    "71": "x^71 + x^54 + x^36 + x^17 + 1",
    "72": "x^72 + x^54 + x^37 + x^21 + 1",
    "73": "x^73 + x^55 + x^36 + x^17 + 1",
    "74": "x^74 + x^56 + x^36 + x^19 + 1",
    "75": "x^75 + x^56 + x^37 + x^20 + 1",
    "76": "x^76 + x^56 + x^36 + x^17 + 1",
    "77": "x^77 + x^56 + x^35 + x^17 + 1",
    "78": "x^78 + x^60 + x^41 + x^21 + 1",
    "79": "x^79 + x^60 + x^40 + x^20 + 1",
    "80": "x^80 + x^59 + x^37 + x^21 + 1",
    "81": "x^81 + x^61 + x^42 + x^22 + 1",
    "82": "x^82 + x^61 + x^39 + x^21 + 1",
    "83": "x^83 + x^63 + x^41 + x^23 + 1",
    "84": "x^84 + x^62 + x^41 + x^20 + 1",
    "85": "x^85 + x^65 + x^46 + x^24 + 1",
    "86": "x^86 + x^63 + x^42 + x^23 + 1",
    "87": "x^87 + x^66 + x^44 + x^21 + 1",
    "88": "x^88 + x^66 + x^45 + x^25 + 1",
    "89": "x^89 + x^68 + x^46 + x^24 + 1",
    "90": "x^90 + x^69 + x^47 + x^24 + 1",
    "91": "x^91 + x^69 + x^48 + x^24 + 1",
    "92": "x^92 + x^70 + x^48 + x^25 + 1",
    "93": "x^93 + x^70 + x^48 + x^25 + 1",
    "94": "x^94 + x^72 + x^47 + x^25 + 1",
    "95": "x^95 + x^71 + x^49 + x^25 + 1",
    "96": "x^96 + x^71 + x^47 + x^21 + 1",
    "97": "x^97 + x^74 + x^49 + x^23 + 1",
    "98": "x^98 + x^74 + x^48 + x^27 + 1",
    "99": "x^99 + x^73 + x^45 + x^22 + 1",
    "100": "x^100 + x^77 + x^53 + x^28 + 1",
    "101": "x^101 + x^75 + x^49 + x^26 + 1",
    "102": "x^102 + x^76 + x^51 + x^27 + 1",
    "103": "x^103 + x^78 + x^54 + x^27 + 1",
    "104": "x^104 + x^78 + x^51 + x^23 + 1",
    "105": "x^105 + x^79 + x^54 + x^27 + 1",
    "106": "x^106 + x^80 + x^55 + x^26 + 1",
    "107": "x^107 + x^83 + x^57 + x^30 + 1",
    "108": "x^108 + x^80 + x^53 + x^25 + 1",
    "109": "x^109 + x^82 + x^54 + x^28 + 1",
    "110": "x^110 + x^82 + x^55 + x^26 + 1",
    "111": "x^111 + x^83 + x^54 + x^26 + 1",
    "112": "x^112 + x^87 + x^58 + x^32 + 1",
    "113": "x^113 + x^84 + x^56 + x^30 + 1",
    "114": "x^114 + x^87 + x^59 + x^30 + 1",
    "115": "x^115 + x^87 + x^60 + x^30 + 1",
    "116": "x^116 + x^88 + x^55 + x^26 + 1",
    "117": "x^117 + x^88 + x^59 + x^29 + 1",
    "118": "x^118 + x^88 + x^61 + x^31 + 1",
    "119": "x^119 + x^89 + x^58 + x^27 + 1",
    "120": "x^120 + x^88 + x^58 + x^27 + 1",
    "121": "x^121 + x^92 + x^61 + x^29 + 1",
    "122": "x^122 + x^92 + x^61 + x^28 + 1",
    "123": "x^123 + x^92 + x^61 + x^28 + 1",
    "124": "x^124 + x^93 + x^61 + x^29 + 1",
    "125": "x^125 + x^92 + x^63 + x^34 + 1",
    "126": "x^126 + x^94 + x^61 + x^29 + 1",
    "127": "x^127 + x^96 + x^65 + x^32 + 1",
    "128": "x^128 + x^95 + x^66 + x^29 + 1",
    "129": "x^129 + x^96 + x^64 + x^30 + 1",
    "130": "x^130 + x^99 + x^65 + x^34 + 1",
    "131": "x^131 + x^98 + x^66 + x^31 + 1",
    "132": "x^132 + x^99 + x^64 + x^34 + 1",
    "133": "x^133 + x^99 + x^64 + x^32 + 1",
    "134": "x^134 + x^101 + x^67 + x^34 + 1",
    "135": "x^135 + x^101 + x^66 + x^36 + 1",
    "136": "x^136 + x^102 + x^71 + x^37 + 1",
    "137": "x^137 + x^103 + x^69 + x^35 + 1",
    "138": "x^138 + x^105 + x^72 + x^37 + 1",
    "139": "x^139 + x^104 + x^70 + x^39 + 1",
    "140": "x^140 + x^105 + x^68 + x^35 + 1",
    "141": "x^141 + x^105 + x^70 + x^36 + 1",
    "142": "x^142 + x^108 + x^73 + x^37 + 1",
    "143": "x^143 + x^107 + x^72 + x^38 + 1",
    "144": "x^144 + x^107 + x^65 + x^31 + 1",
    "145": "x^145 + x^109 + x^75 + x^38 + 1",
    "146": "x^146 + x^110 + x^71 + x^38 + 1",
    "147": "x^147 + x^109 + x^73 + x^39 + 1",
    "148": "x^148 + x^111 + x^71 + x^35 + 1",
    "149": "x^149 + x^111 + x^72 + x^36 + 1",
    "150": "x^150 + x^113 + x^74 + x^40 + 1",
    "151": "x^151 + x^113 + x^74 + x^39 + 1",
    "152": "x^152 + x^117 + x^83 + x^43 + 1",
    "153": "x^153 + x^114 + x^75 + x^37 + 1",
    "154": "x^154 + x^116 + x^79 + x^39 + 1",
    "155": "x^155 + x^116 + x^78 + x^39 + 1",
    "156": "x^156 + x^118 + x^79 + x^41 + 1",
    "157": "x^157 + x^118 + x^81 + x^41 + 1",
    "158": "x^158 + x^119 + x^81 + x^41 + 1",
    "159": "x^159 + x^119 + x^82 + x^41 + 1",
    "160": "x^160 + x^119 + x^81 + x^43 + 1",
    "161": "x^161 + x^121 + x^79 + x^39 + 1",
    "162": "x^162 + x^122 + x^83 + x^39 + 1",
    "163": "x^163 + x^123 + x^82 + x^43 + 1",
    "164": "x^164 + x^125 + x^86 + x^44 + 1",
    "165": "x^165 + x^125 + x^83 + x^38 + 1",
    "166": "x^166 + x^125 + x^82 + x^38 + 1",
    "167": "x^167 + x^125 + x^85 + x^42 + 1",
    "168": "x^168 + x^126 + x^83 + x^41 + 1",
    "169": "x^169 + x^125 + x^80 + x^40 + 1",
    "170": "x^170 + x^128 + x^83 + x^41 + 1",
    "171": "x^171 + x^129 + x^88 + x^45 + 1",
    "172": "x^172 + x^129 + x^85 + x^44 + 1",
    "173": "x^173 + x^130 + x^88 + x^45 + 1",
    "174": "x^174 + x^129 + x^83 + x^39 + 1",
    "175": "x^175 + x^132 + x^85 + x^45 + 1",
    "176": "x^176 + x^133 + x^93 + x^50 + 1",
    "177": "x^177 + x^132 + x^87 + x^43 + 1",
    "178": "x^178 + x^134 + x^89 + x^42 + 1",
    "179": "x^179 + x^135 + x^94 + x^47 + 1",
    "180": "x^180 + x^137 + x^90 + x^42 + 1",
    "181": "x^181 + x^136 + x^91 + x^45 + 1",
    "182": "x^182 + x^137 + x^90 + x^47 + 1",
    "183": "x^183 + x^137 + x^90 + x^42 + 1",
    "184": "x^184 + x^141 + x^91 + x^40 + 1",
    "185": "x^185 + x^138 + x^89 + x^45 + 1",
    "186": "x^186 + x^138 + x^91 + x^48 + 1",
    "187": "x^187 + x^139 + x^90 + x^44 + 1",
    "188": "x^188 + x^142 + x^91 + x^45 + 1",
    "189": "x^189 + x^142 + x^92 + x^43 + 1",
    "190": "x^190 + x^142 + x^97 + x^51 + 1",
    "191": "x^191 + x^144 + x^98 + x^49 + 1",
    "192": "x^192 + x^146 + x^95 + x^43 + 1",
    "193": "x^193 + x^146 + x^100 + x^50 + 1",
    "194": "x^194 + x^145 + x^98 + x^51 + 1",
    "195": "x^195 + x^142 + x^89 + x^43 + 1",
    "196": "x^196 + x^148 + x^101 + x^51 + 1",
    "197": "x^197 + x^148 + x^99 + x^49 + 1",
    "198": "x^198 + x^148 + x^101 + x^52 + 1",
    "199": "x^199 + x^150 + x^101 + x^49 + 1",
    "200": "x^200 + x^155 + x^100 + x^57 + 1",
    "201": "x^201 + x^149 + x^102 + x^54 + 1",
    "202": "x^202 + x^151 + x^96 + x^49 + 1",
    "203": "x^203 + x^154 + x^102 + x^49 + 1",
    "204": "x^204 + x^153 + x^105 + x^53 + 1",
    "205": "x^205 + x^153 + x^102 + x^52 + 1",
    "206": "x^206 + x^154 + x^105 + x^53 + 1",
    "207": "x^207 + x^156 + x^102 + x^50 + 1",
    "208": "x^208 + x^155 + x^100 + x^53 + 1",
    "209": "x^209 + x^158 + x^105 + x^54 + 1",
    "210": "x^210 + x^157 + x^107 + x^55 + 1",
    "211": "x^211 + x^157 + x^105 + x^55 + 1",
    "212": "x^212 + x^159 + x^106 + x^55 + 1",
    "213": "x^213 + x^159 + x^101 + x^48 + 1",
    "214": "x^214 + x^161 + x^108 + x^53 + 1",
    "215": "x^215 + x^162 + x^110 + x^55 + 1",
    "216": "x^216 + x^163 + x^115 + x^57 + 1",
    "217": "x^217 + x^165 + x^109 + x^52 + 1",
    "218": "x^218 + x^165 + x^111 + x^56 + 1",
    "219": "x^219 + x^164 + x^110 + x^53 + 1",
    "220": "x^220 + x^163 + x^105 + x^53 + 1",
    "221": "x^221 + x^166 + x^114 + x^59 + 1",
    "222": "x^222 + x^166 + x^113 + x^58 + 1",
    "223": "x^223 + x^168 + x^116 + x^58 + 1",
    "224": "x^224 + x^167 + x^114 + x^51 + 1",
    "225": "x^225 + x^167 + x^110 + x^54 + 1",
    "226": "x^226 + x^170 + x^115 + x^56 + 1",
    "227": "x^227 + x^172 + x^114 + x^59 + 1",
    "228": "x^228 + x^170 + x^112 + x^55 + 1",
    "229": "x^229 + x^172 + x^115 + x^55 + 1",
    "230": "x^230 + x^173 + x^110 + x^54 + 1",
    "231": "x^231 + x^174 + x^113 + x^56 + 1",
    "232": "x^232 + x^173 + x^117 + x^55 + 1",
    "233": "x^233 + x^174 + x^116 + x^56 + 1",
    "234": "x^234 + x^175 + x^116 + x^59 + 1",
    "235": "x^235 + x^178 + x^123 + x^62 + 1",
    "236": "x^236 + x^175 + x^113 + x^57 + 1",
    "237": "x^237 + x^178 + x^118 + x^60 + 1",
    "238": "x^238 + x^180 + x^119 + x^61 + 1",
    "239": "x^239 + x^179 + x^118 + x^58 + 1",
    "240": "x^240 + x^185 + x^131 + x^67 + 1",
    "241": "x^241 + x^181 + x^121 + x^60 + 1",
    "242": "x^242 + x^181 + x^119 + x^61 + 1",
    "243": "x^243 + x^185 + x^130 + x^65 + 1",
    "244": "x^244 + x^182 + x^121 + x^60 + 1",
    "245": "x^245 + x^186 + x^125 + x^64 + 1",
    "246": "x^246 + x^189 + x^125 + x^66 + 1",
    "247": "x^247 + x^186 + x^121 + x^60 + 1",
    "248": "x^248 + x^185 + x^127 + x^64 + 1",
    "249": "x^249 + x^186 + x^124 + x^63 + 1",
    "250": "x^250 + x^187 + x^126 + x^66 + 1",
    "251": "x^251 + x^188 + x^124 + x^61 + 1",
    "252": "x^252 + x^189 + x^124 + x^61 + 1",
    "253": "x^253 + x^190 + x^130 + x^63 + 1",
    "254": "x^254 + x^189 + x^127 + x^61 + 1",
    "255": "x^255 + x^189 + x^129 + x^67 + 1",
    "256": "x^256 + x^196 + x^131 + x^69 + 1",
    "257": "x^257 + x^193 + x^129 + x^65 + 1",
    "258": "x^258 + x^195 + x^129 + x^67 + 1",
    "259": "x^259 + x^196 + x^132 + x^69 + 1",
    "260": "x^260 + x^195 + x^131 + x^67 + 1",
    "261": "x^261 + x^192 + x^127 + x^61 + 1",
    "262": "x^262 + x^195 + x^133 + x^62 + 1",
    "263": "x^263 + x^197 + x^131 + x^62 + 1",
    "264": "x^264 + x^197 + x^128 + x^63 + 1",
    "265": "x^265 + x^199 + x^135 + x^67 + 1",
    "266": "x^266 + x^200 + x^133 + x^64 + 1",
    "267": "x^267 + x^201 + x^129 + x^67 + 1",
    "268": "x^268 + x^201 + x^132 + x^67 + 1",
    "269": "x^269 + x^199 + x^134 + x^70 + 1",
    "270": "x^270 + x^200 + x^133 + x^64 + 1",
    "271": "x^271 + x^204 + x^137 + x^70 + 1",
    "272": "x^272 + x^203 + x^133 + x^69 + 1",
    "273": "x^273 + x^206 + x^140 + x^70 + 1",
    "274": "x^274 + x^206 + x^137 + x^69 + 1",
    "275": "x^275 + x^207 + x^138 + x^71 + 1",
    "276": "x^276 + x^207 + x^136 + x^70 + 1",
    "277": "x^277 + x^210 + x^139 + x^67 + 1",
    "278": "x^278 + x^209 + x^137 + x^72 + 1",
    "279": "x^279 + x^209 + x^142 + x^71 + 1",
    "280": "x^280 + x^213 + x^142 + x^74 + 1",
    "281": "x^281 + x^210 + x^140 + x^71 + 1",
    "282": "x^282 + x^212 + x^141 + x^71 + 1",
    "283": "x^283 + x^212 + x^141 + x^67 + 1",
    "284": "x^284 + x^211 + x^139 + x^66 + 1",
    "285": "x^285 + x^214 + x^144 + x^73 + 1",
    "286": "x^286 + x^216 + x^143 + x^68 + 1",
    "287": "x^287 + x^216 + x^144 + x^72 + 1",
    "288": "x^288 + x^216 + x^139 + x^69 + 1",
    "289": "x^289 + x^218 + x^145 + x^71 + 1",
    "290": "x^290 + x^218 + x^143 + x^71 + 1",
    "291": "x^291 + x^215 + x^144 + x^77 + 1",
    "292": "x^292 + x^222 + x^149 + x^77 + 1",
    "293": "x^293 + x^219 + x^145 + x^70 + 1",
    "294": "x^294 + x^219 + x^145 + x^75 + 1",
    "295": "x^295 + x^223 + x^147 + x^71 + 1",
    "296": "x^296 + x^223 + x^153 + x^82 + 1",
    "297": "x^297 + x^224 + x^150 + x^77 + 1",
    "298": "x^298 + x^225 + x^150 + x^72 + 1",
    "299": "x^299 + x^222 + x^149 + x^70 + 1",
    "300": "x^300 + x^225 + x^149 + x^75 + 1",
    "301": "x^301 + x^224 + x^151 + x^72 + 1",
    "302": "x^302 + x^227 + x^155 + x^77 + 1",
    "303": "x^303 + x^226 + x^156 + x^79 + 1",
    "304": "x^304 + x^225 + x^151 + x^79 + 1",
    "305": "x^305 + x^227 + x^152 + x^74 + 1",
    "306": "x^306 + x^230 + x^153 + x^72 + 1",
    "307": "x^307 + x^231 + x^156 + x^81 + 1",
    "308": "x^308 + x^230 + x^155 + x^80 + 1",
    "309": "x^309 + x^230 + x^150 + x^75 + 1",
    "310": "x^310 + x^232 + x^155 + x^74 + 1",
    "311": "x^311 + x^233 + x^158 + x^80 + 1",
    "312": "x^312 + x^235 + x^154 + x^81 + 1",
    "313": "x^313 + x^235 + x^157 + x^79 + 1",
    "314": "x^314 + x^236 + x^157 + x^76 + 1",
    "315": "x^315 + x^237 + x^161 + x^80 + 1",
    "316": "x^316 + x^239 + x^159 + x^82 + 1",
    "317": "x^317 + x^237 + x^158 + x^80 + 1",
    "318": "x^318 + x^240 + x^161 + x^83 + 1",
    "319": "x^319 + x^238 + x^155 + x^77 + 1",
    "320": "x^320 + x^241 + x^165 + x^86 + 1",
    "321": "x^321 + x^241 + x^161 + x^80 + 1",
    "322": "x^322 + x^242 + x^160 + x^83 + 1",
    "323": "x^323 + x^241 + x^155 + x^76 + 1",
    "324": "x^324 + x^248 + x^167 + x^88 + 1",
    "325": "x^325 + x^243 + x^160 + x^80 + 1",
    "326": "x^326 + x^244 + x^167 + x^79 + 1",
    "327": "x^327 + x^245 + x^165 + x^83 + 1",
    "328": "x^328 + x^244 + x^165 + x^87 + 1",
    "329": "x^329 + x^247 + x^166 + x^84 + 1",
    "330": "x^330 + x^248 + x^165 + x^83 + 1",
    "331": "x^331 + x^248 + x^163 + x^81 + 1",
    "332": "x^332 + x^250 + x^163 + x^81 + 1",
    "333": "x^333 + x^248 + x^163 + x^85 + 1",
    "334": "x^334 + x^250 + x^167 + x^87 + 1",
    "335": "x^335 + x^252 + x^168 + x^83 + 1",
    "336": "x^336 + x^253 + x^174 + x^81 + 1",
    "337": "x^337 + x^254 + x^169 + x^86 + 1",
    "338": "x^338 + x^255 + x^173 + x^87 + 1",
    "339": "x^339 + x^254 + x^173 + x^87 + 1",
    "340": "x^340 + x^255 + x^165 + x^84 + 1",
    "341": "x^341 + x^258 + x^171 + x^83 + 1",
    "342": "x^342 + x^257 + x^168 + x^84 + 1",
    "343": "x^343 + x^257 + x^173 + x^87 + 1",
    "344": "x^344 + x^258 + x^173 + x^87 + 1",
    "345": "x^345 + x^257 + x^171 + x^83 + 1",
    "346": "x^346 + x^258 + x^173 + x^82 + 1",
    "347": "x^347 + x^262 + x^174 + x^89 + 1",
    "348": "x^348 + x^257 + x^175 + x^92 + 1",
    "349": "x^349 + x^260 + x^174 + x^85 + 1",
    "350": "x^350 + x^261 + x^173 + x^84 + 1",
    "351": "x^351 + x^262 + x^172 + x^89 + 1",
    "352": "x^352 + x^262 + x^178 + x^91 + 1",
    "353": "x^353 + x^263 + x^174 + x^86 + 1",
    "354": "x^354 + x^269 + x^183 + x^92 + 1",
    "355": "x^355 + x^263 + x^180 + x^94 + 1",
    "356": "x^356 + x^266 + x^181 + x^91 + 1",
    "357": "x^357 + x^266 + x^178 + x^91 + 1",
    "358": "x^358 + x^272 + x^179 + x^93 + 1",
    "359": "x^359 + x^270 + x^180 + x^89 + 1",
    "360": "x^360 + x^273 + x^175 + x^81 + 1",
    "361": "x^361 + x^272 + x^179 + x^87 + 1",
    "362": "x^362 + x^272 + x^183 + x^92 + 1",
    "363": "x^363 + x^274 + x^183 + x^87 + 1",
    "364": "x^364 + x^273 + x^184 + x^93 + 1",
    "365": "x^365 + x^273 + x^182 + x^93 + 1",
    "366": "x^366 + x^276 + x^186 + x^89 + 1",
    "367": "x^367 + x^276 + x^186 + x^91 + 1",
    "368": "x^368 + x^277 + x^187 + x^86 + 1",
    "369": "x^369 + x^277 + x^183 + x^94 + 1",
    "370": "x^370 + x^281 + x^191 + x^96 + 1",
    "371": "x^371 + x^278 + x^186 + x^89 + 1",
    "372": "x^372 + x^278 + x^185 + x^91 + 1",
    "373": "x^373 + x^280 + x^181 + x^87 + 1",
    "374": "x^374 + x^281 + x^185 + x^90 + 1",
    "375": "x^375 + x^280 + x^190 + x^96 + 1",
    "376": "x^376 + x^281 + x^187 + x^90 + 1",
    "377": "x^377 + x^285 + x^189 + x^98 + 1",
    "378": "x^378 + x^283 + x^187 + x^96 + 1",
    "379": "x^379 + x^284 + x^189 + x^91 + 1",
    "380": "x^380 + x^285 + x^188 + x^93 + 1",
    "381": "x^381 + x^290 + x^193 + x^100 + 1",
    "382": "x^382 + x^285 + x^190 + x^93 + 1",
    "383": "x^383 + x^286 + x^187 + x^92 + 1",
    "384": "x^384 + x^284 + x^197 + x^91 + 1",
    "385": "x^385 + x^290 + x^195 + x^98 + 1",
    "386": "x^386 + x^290 + x^193 + x^94 + 1",
    "387": "x^387 + x^290 + x^194 + x^95 + 1",
    "388": "x^388 + x^293 + x^195 + x^94 + 1",
    "389": "x^389 + x^291 + x^197 + x^100 + 1",
    "390": "x^390 + x^293 + x^196 + x^97 + 1",
    "391": "x^391 + x^294 + x^194 + x^95 + 1",
    "392": "x^392 + x^298 + x^203 + x^105 + 1",
    "393": "x^393 + x^295 + x^199 + x^95 + 1",
    "394": "x^394 + x^296 + x^196 + x^95 + 1",
    "395": "x^395 + x^296 + x^194 + x^101 + 1",
    "396": "x^396 + x^297 + x^194 + x^95 + 1",
    "397": "x^397 + x^297 + x^194 + x^95 + 1",
    "398": "x^398 + x^295 + x^192 + x^94 + 1",
    "399": "x^399 + x^295 + x^197 + x^94 + 1",
    "400": "x^400 + x^299 + x^198 + x^95 + 1",
    "401": "x^401 + x^300 + x^203 + x^103 + 1",
    "402": "x^402 + x^299 + x^200 + x^104 + 1",
    "403": "x^403 + x^301 + x^201 + x^104 + 1",
    "404": "x^404 + x^301 + x^203 + x^96 + 1",
    "405": "x^405 + x^307 + x^212 + x^106 + 1",
    "406": "x^406 + x^305 + x^207 + x^103 + 1",
    "407": "x^407 + x^307 + x^204 + x^104 + 1",
    "408": "x^408 + x^301 + x^205 + x^95 + 1",
    "409": "x^409 + x^304 + x^204 + x^105 + 1",
    "410": "x^410 + x^308 + x^205 + x^97 + 1",
    "411": "x^411 + x^310 + x^205 + x^107 + 1",
    "412": "x^412 + x^309 + x^205 + x^104 + 1",
    "413": "x^413 + x^309 + x^203 + x^100 + 1",
    "414": "x^414 + x^312 + x^209 + x^107 + 1",
    "415": "x^415 + x^312 + x^205 + x^105 + 1",
    "416": "x^416 + x^315 + x^210 + x^101 + 1",
    "417": "x^417 + x^312 + x^208 + x^103 + 1",
    "418": "x^418 + x^315 + x^211 + x^106 + 1",
    "419": "x^419 + x^315 + x^209 + x^101 + 1",
    "420": "x^420 + x^317 + x^209 + x^109 + 1",
    "421": "x^421 + x^314 + x^207 + x^101 + 1",
    "422": "x^422 + x^315 + x^208 + x^103 + 1",
    "423": "x^423 + x^316 + x^208 + x^107 + 1",
    "424": "x^424 + x^318 + x^210 + x^103 + 1",
    "425": "x^425 + x^317 + x^210 + x^103 + 1",
    "426": "x^426 + x^319 + x^215 + x^109 + 1",
    "427": "x^427 + x^321 + x^213 + x^108 + 1",
    "428": "x^428 + x^322 + x^215 + x^109 + 1",
    "429": "x^429 + x^322 + x^217 + x^105 + 1",
    "430": "x^430 + x^322 + x^214 + x^105 + 1",
    "431": "x^431 + x^324 + x^213 + x^104 + 1",
    "432": "x^432 + x^321 + x^207 + x^100 + 1",
    "433": "x^433 + x^326 + x^216 + x^106 + 1",
    "434": "x^434 + x^324 + x^216 + x^111 + 1",
    "435": "x^435 + x^326 + x^215 + x^107 + 1",
    "436": "x^436 + x^328 + x^219 + x^108 + 1",
    "437": "x^437 + x^330 + x^216 + x^105 + 1",
    "438": "x^438 + x^329 + x^221 + x^110 + 1",
    "439": "x^439 + x^331 + x^225 + x^113 + 1",
    "440": "x^440 + x^331 + x^222 + x^115 + 1",
    "441": "x^441 + x^331 + x^223 + x^110 + 1",
    "442": "x^442 + x^332 + x^216 + x^107 + 1",
    "443": "x^443 + x^333 + x^224 + x^112 + 1",
    "444": "x^444 + x^333 + x^223 + x^109 + 1",
    "445": "x^445 + x^334 + x^222 + x^109 + 1",
    "446": "x^446 + x^334 + x^219 + x^109 + 1",
    "447": "x^447 + x^337 + x^223 + x^114 + 1",
    "448": "x^448 + x^339 + x^234 + x^117 + 1",
    "449": "x^449 + x^335 + x^222 + x^110 + 1",
    "450": "x^450 + x^342 + x^234 + x^119 + 1",
    "451": "x^451 + x^337 + x^221 + x^114 + 1",
    "452": "x^452 + x^339 + x^229 + x^112 + 1",
    "453": "x^453 + x^342 + x^227 + x^117 + 1",
    "454": "x^454 + x^341 + x^228 + x^113 + 1",
    "455": "x^455 + x^341 + x^230 + x^116 + 1",
    "456": "x^456 + x^338 + x^217 + x^107 + 1",
    "457": "x^457 + x^344 + x^230 + x^118 + 1",
    "458": "x^458 + x^345 + x^233 + x^116 + 1",
    "459": "x^459 + x^344 + x^230 + x^119 + 1",
    "460": "x^460 + x^347 + x^235 + x^119 + 1",
    "461": "x^461 + x^345 + x^230 + x^110 + 1",
    "462": "x^462 + x^344 + x^227 + x^110 + 1",
    "463": "x^463 + x^347 + x^232 + x^116 + 1",
    "464": "x^464 + x^347 + x^237 + x^120 + 1",
    "465": "x^465 + x^349 + x^233 + x^119 + 1",
    "466": "x^466 + x^348 + x^235 + x^119 + 1",
    "467": "x^467 + x^350 + x^234 + x^120 + 1",
    "468": "x^468 + x^352 + x^235 + x^119 + 1",
    "469": "x^469 + x^352 + x^236 + x^119 + 1",
    "470": "x^470 + x^350 + x^233 + x^113 + 1",
    "471": "x^471 + x^354 + x^238 + x^121 + 1",
    "472": "x^472 + x^350 + x^237 + x^125 + 1",
    "473": "x^473 + x^356 + x^236 + x^120 + 1",
    "474": "x^474 + x^355 + x^236 + x^115 + 1",
    "475": "x^475 + x^354 + x^237 + x^114 + 1",
    "476": "x^476 + x^353 + x^232 + x^115 + 1",
    "477": "x^477 + x^359 + x^242 + x^118 + 1",
    "478": "x^478 + x^358 + x^237 + x^114 + 1",
    "479": "x^479 + x^360 + x^241 + x^122 + 1",
    "480": "x^480 + x^363 + x^239 + x^125 + 1",
    "481": "x^481 + x^362 + x^241 + x^122 + 1",
    "482": "x^482 + x^362 + x^240 + x^123 + 1",
    "483": "x^483 + x^363 + x^238 + x^117 + 1",
    "484": "x^484 + x^366 + x^242 + x^115 + 1",
    "485": "x^485 + x^367 + x^250 + x^125 + 1",
    "486": "x^486 + x^363 + x^241 + x^124 + 1",
    "487": "x^487 + x^367 + x^248 + x^123 + 1",
    "488": "x^488 + x^367 + x^245 + x^126 + 1",
    "489": "x^489 + x^365 + x^245 + x^125 + 1",
    "490": "x^490 + x^369 + x^246 + x^121 + 1",
    "491": "x^491 + x^365 + x^245 + x^126 + 1",
    "492": "x^492 + x^370 + x^247 + x^122 + 1",
    "493": "x^493 + x^371 + x^250 + x^126 + 1",
    "494": "x^494 + x^373 + x^255 + x^127 + 1",
    "495": "x^495 + x^371 + x^244 + x^119 + 1",
    "496": "x^496 + x^375 + x^250 + x^129 + 1",
    "497": "x^497 + x^374 + x^250 + x^126 + 1",
    "498": "x^498 + x^374 + x^251 + x^126 + 1",
    "499": "x^499 + x^374 + x^246 + x^119 + 1",
    "500": "x^500 + x^373 + x^250 + x^122 + 1",
    "501": "x^501 + x^376 + x^246 + x^126 + 1",
    "502": "x^502 + x^381 + x^262 + x^132 + 1",
    "503": "x^503 + x^378 + x^248 + x^121 + 1",
    "504": "x^504 + x^382 + x^251 + x^121 + 1",
    "505": "x^505 + x^381 + x^255 + x^130 + 1",
    "506": "x^506 + x^378 + x^247 + x^122 + 1",
    "507": "x^507 + x^382 + x^261 + x^132 + 1",
    "508": "x^508 + x^381 + x^250 + x^123 + 1",
    "509": "x^509 + x^383 + x^255 + x^124 + 1",
    "510": "x^510 + x^385 + x^265 + x^133 + 1",
    "511": "x^511 + x^385 + x^257 + x^129 + 1",
    "512": "x^512 + x^387 + x^257 + x^124 + 1",
    "513": "x^513 + x^385 + x^257 + x^128 + 1",
    "514": "x^514 + x^387 + x^254 + x^124 + 1",
    "515": "x^515 + x^387 + x^258 + x^126 + 1",
    "516": "x^516 + x^387 + x^258 + x^127 + 1",
    "517": "x^517 + x^388 + x^259 + x^127 + 1",
    "518": "x^518 + x^390 + x^261 + x^131 + 1",
    "519": "x^519 + x^390 + x^264 + x^133 + 1",
    "520": "x^520 + x^387 + x^248 + x^125 + 1",
    "521": "x^521 + x^391 + x^263 + x^130 + 1",
    "522": "x^522 + x^390 + x^258 + x^127 + 1",
    "523": "x^523 + x^393 + x^262 + x^133 + 1",
    "524": "x^524 + x^390 + x^257 + x^127 + 1",
    "525": "x^525 + x^395 + x^262 + x^136 + 1",
    "526": "x^526 + x^395 + x^264 + x^134 + 1",
    "527": "x^527 + x^394 + x^263 + x^129 + 1",
    "528": "x^528 + x^392 + x^263 + x^137 + 1",
    "529": "x^529 + x^396 + x^262 + x^131 + 1",
    "530": "x^530 + x^400 + x^267 + x^128 + 1",
    "531": "x^531 + x^401 + x^266 + x^130 + 1",
    "532": "x^532 + x^399 + x^268 + x^138 + 1",
    "533": "x^533 + x^400 + x^267 + x^137 + 1",
    "534": "x^534 + x^401 + x^267 + x^137 + 1",
    "535": "x^535 + x^399 + x^263 + x^130 + 1",
    "536": "x^536 + x^401 + x^263 + x^131 + 1",
    "537": "x^537 + x^400 + x^269 + x^140 + 1",
    "538": "x^538 + x^405 + x^271 + x^138 + 1",
    "539": "x^539 + x^405 + x^276 + x^140 + 1",
    "540": "x^540 + x^404 + x^268 + x^133 + 1",
    "541": "x^541 + x^404 + x^273 + x^139 + 1",
    "542": "x^542 + x^408 + x^269 + x^138 + 1",
    "543": "x^543 + x^406 + x^269 + x^133 + 1",
    "544": "x^544 + x^411 + x^274 + x^140 + 1",
    "545": "x^545 + x^407 + x^269 + x^134 + 1",
    "546": "x^546 + x^411 + x^275 + x^140 + 1",
    "547": "x^547 + x^409 + x^274 + x^139 + 1",
    "548": "x^548 + x^411 + x^278 + x^140 + 1",
    "549": "x^549 + x^410 + x^273 + x^131 + 1",
    "550": "x^550 + x^412 + x^276 + x^139 + 1",
    "551": "x^551 + x^416 + x^275 + x^141 + 1",
    "552": "x^552 + x^413 + x^268 + x^131 + 1",
    "553": "x^553 + x^414 + x^275 + x^140 + 1",
    "554": "x^554 + x^416 + x^275 + x^132 + 1",
    "555": "x^555 + x^418 + x^281 + x^143 + 1",
    "556": "x^556 + x^416 + x^276 + x^137 + 1",
    "557": "x^557 + x^415 + x^269 + x^136 + 1",
    "558": "x^558 + x^421 + x^279 + x^136 + 1",
    "559": "x^559 + x^420 + x^281 + x^140 + 1",
    "560": "x^560 + x^419 + x^282 + x^137 + 1",
    "561": "x^561 + x^420 + x^279 + x^139 + 1",
    "562": "x^562 + x^421 + x^277 + x^135 + 1",
    "563": "x^563 + x^426 + x^286 + x^145 + 1",
    "564": "x^564 + x^420 + x^277 + x^138 + 1",
    "565": "x^565 + x^422 + x^282 + x^143 + 1",
    "566": "x^566 + x^422 + x^281 + x^146 + 1",
    "567": "x^567 + x^427 + x^287 + x^145 + 1",
    "568": "x^568 + x^423 + x^282 + x^147 + 1",
    "569": "x^569 + x^426 + x^282 + x^140 + 1",
    "570": "x^570 + x^427 + x^279 + x^141 + 1",
    "571": "x^571 + x^429 + x^286 + x^141 + 1",
    "572": "x^572 + x^427 + x^286 + x^146 + 1",
    "573": "x^573 + x^430 + x^283 + x^141 + 1",
    "574": "x^574 + x^430 + x^287 + x^146 + 1",
    "575": "x^575 + x^432 + x^289 + x^146 + 1",
    "576": "x^576 + x^432 + x^279 + x^137 + 1",
    "577": "x^577 + x^437 + x^292 + x^149 + 1",
    "578": "x^578 + x^434 + x^291 + x^146 + 1",
    "579": "x^579 + x^436 + x^288 + x^141 + 1",
    "580": "x^580 + x^436 + x^290 + x^147 + 1",
    "581": "x^581 + x^437 + x^291 + x^143 + 1",
    "582": "x^582 + x^434 + x^284 + x^141 + 1",
    "583": "x^583 + x^436 + x^293 + x^143 + 1",
    "584": "x^584 + x^441 + x^294 + x^150 + 1",
    "585": "x^585 + x^439 + x^292 + x^148 + 1",
    "586": "x^586 + x^441 + x^293 + x^140 + 1",
    "587": "x^587 + x^437 + x^291 + x^142 + 1",
    "588": "x^588 + x^438 + x^284 + x^141 + 1",
    "589": "x^589 + x^440 + x^295 + x^152 + 1",
    "590": "x^590 + x^443 + x^293 + x^143 + 1",
    "591": "x^591 + x^444 + x^294 + x^145 + 1",
    "592": "x^592 + x^442 + x^293 + x^153 + 1",
    "593": "x^593 + x^444 + x^293 + x^145 + 1",
    "594": "x^594 + x^447 + x^295 + x^151 + 1",
    "595": "x^595 + x^445 + x^294 + x^143 + 1",
    "596": "x^596 + x^448 + x^296 + x^147 + 1",
    "597": "x^597 + x^445 + x^301 + x^154 + 1",
    "598": "x^598 + x^448 + x^299 + x^152 + 1",
    "599": "x^599 + x^450 + x^300 + x^152 + 1",
    "600": "x^600 + x^451 + x^293 + x^146 + 1",
    "601": "x^601 + x^450 + x^299 + x^149 + 1",
    "602": "x^602 + x^449 + x^298 + x^153 + 1",
    "603": "x^603 + x^450 + x^295 + x^145 + 1",
    "604": "x^604 + x^459 + x^305 + x^158 + 1",
    "605": "x^605 + x^454 + x^306 + x^155 + 1",
    "606": "x^606 + x^453 + x^301 + x^153 + 1",
    "607": "x^607 + x^455 + x^304 + x^150 + 1",
    "608": "x^608 + x^455 + x^305 + x^159 + 1",
    "609": "x^609 + x^457 + x^304 + x^157 + 1",
    "610": "x^610 + x^457 + x^305 + x^158 + 1",
    "611": "x^611 + x^459 + x^308 + x^153 + 1",
    "612": "x^612 + x^462 + x^305 + x^149 + 1",
    "613": "x^613 + x^458 + x^310 + x^156 + 1",
    "614": "x^614 + x^459 + x^306 + x^155 + 1",
    "615": "x^615 + x^461 + x^312 + x^156 + 1",
    "616": "x^616 + x^463 + x^311 + x^149 + 1",
    "617": "x^617 + x^464 + x^309 + x^156 + 1",
    "618": "x^618 + x^463 + x^305 + x^155 + 1",
    "619": "x^619 + x^469 + x^315 + x^160 + 1",
    "620": "x^620 + x^465 + x^305 + x^154 + 1",
    "621": "x^621 + x^466 + x^310 + x^160 + 1",
    "622": "x^622 + x^462 + x^309 + x^150 + 1",
    "623": "x^623 + x^466 + x^310 + x^158 + 1",
    "624": "x^624 + x^473 + x^316 + x^151 + 1",
    "625": "x^625 + x^470 + x^310 + x^153 + 1",
    "626": "x^626 + x^474 + x^313 + x^161 + 1",
    "627": "x^627 + x^470 + x^314 + x^158 + 1",
    "628": "x^628 + x^469 + x^311 + x^159 + 1",
    "629": "x^629 + x^471 + x^313 + x^158 + 1",
    "630": "x^630 + x^471 + x^316 + x^163 + 1",
    "631": "x^631 + x^472 + x^314 + x^155 + 1",
    "632": "x^632 + x^473 + x^317 + x^150 + 1",
    "633": "x^633 + x^472 + x^316 + x^161 + 1",
    "634": "x^634 + x^477 + x^318 + x^157 + 1",
    "635": "x^635 + x^477 + x^315 + x^155 + 1",
    "636": "x^636 + x^476 + x^315 + x^161 + 1",
    "637": "x^637 + x^476 + x^315 + x^155 + 1",
    "638": "x^638 + x^477 + x^319 + x^163 + 1",
    "639": "x^639 + x^481 + x^326 + x^164 + 1",
    "640": "x^640 + x^475 + x^316 + x^165 + 1",
    "641": "x^641 + x^482 + x^326 + x^162 + 1",
    "642": "x^642 + x^482 + x^322 + x^167 + 1",
    "643": "x^643 + x^483 + x^317 + x^158 + 1",
    "644": "x^644 + x^482 + x^321 + x^160 + 1",
    "645": "x^645 + x^476 + x^318 + x^153 + 1",
    "646": "x^646 + x^486 + x^329 + x^163 + 1",
    "647": "x^647 + x^485 + x^326 + x^164 + 1",
    "648": "x^648 + x^489 + x^318 + x^155 + 1",
    "649": "x^649 + x^490 + x^331 + x^166 + 1",
    "650": "x^650 + x^486 + x^324 + x^159 + 1",
    "651": "x^651 + x^490 + x^331 + x^165 + 1",
    "652": "x^652 + x^490 + x^328 + x^165 + 1",
    "653": "x^653 + x^490 + x^328 + x^165 + 1",
    "654": "x^654 + x^491 + x^330 + x^165 + 1",
    "655": "x^655 + x^491 + x^329 + x^166 + 1",
    "656": "x^656 + x^487 + x^329 + x^171 + 1",
    "657": "x^657 + x^489 + x^328 + x^169 + 1",
    "658": "x^658 + x^496 + x^327 + x^160 + 1",
    "659": "x^659 + x^494 + x^330 + x^162 + 1",
    "660": "x^660 + x^496 + x^331 + x^162 + 1"
}