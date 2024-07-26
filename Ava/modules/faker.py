import random
import string
from faker import Faker
from pyrogram import filters
from Ava import Jarvis as app

# Mapping of country codes to country names
COUNTRY_CODES = {
    "ad": "Andorra", "ae": "United Arab Emirates", "af": "Afghanistan",
    "ag": "Antigua and Barbuda", "ai": "Anguilla", "al": "Albania",
    "am": "Armenia", "ao": "Angola", "aq": "Antarctica", "ar": "Argentina",
    "as": "American Samoa", "at": "Austria", "au": "Australia", "aw": "Aruba",
    "ax": "Åland Islands", "az": "Azerbaijan", "ba": "Bosnia and Herzegovina",
    "bb": "Barbados", "bd": "Bangladesh", "be": "Belgium", "bf": "Burkina Faso",
    "bg": "Bulgaria", "bh": "Bahrain", "bi": "Burundi", "bj": "Benin",
    "bl": "Saint Barthélemy", "bm": "Bermuda", "bn": "Brunei Darussalam",
    "bo": "Bolivia", "bq": "Bonaire, Sint Eustatius and Saba", "br": "Brazil",
    "bs": "Bahamas", "bt": "Bhutan", "bv": "Bouvet Island", "bw": "Botswana",
    "by": "Belarus", "bz": "Belize", "ca": "Canada", "cc": "Cocos (Keeling) Islands",
    "cd": "Congo, Democratic Republic of the", "cf": "Central African Republic",
    "cg": "Congo", "ch": "Switzerland", "ci": "Côte d'Ivoire", "ck": "Cook Islands",
    "cl": "Chile", "cm": "Cameroon", "cn": "China", "co": "Colombia",
    "cr": "Costa Rica", "cu": "Cuba", "cv": "Cabo Verde", "cw": "Curaçao",
    "cx": "Christmas Island", "cy": "Cyprus", "cz": "Czechia", "de": "Germany",
    "dj": "Djibouti", "dk": "Denmark", "dm": "Dominica", "do": "Dominican Republic",
    "dz": "Algeria", "ec": "Ecuador", "ee": "Estonia", "eg": "Egypt",
    "eh": "Western Sahara", "er": "Eritrea", "es": "Spain", "et": "Ethiopia",
    "fi": "Finland", "fj": "Fiji", "fm": "Micronesia", "fo": "Faroe Islands",
    "fr": "France", "ga": "Gabon", "gb": "United Kingdom", "gd": "Grenada",
    "ge": "Georgia", "gf": "French Guiana", "gg": "Guernsey", "gh": "Ghana",
    "gi": "Gibraltar", "gl": "Greenland", "gm": "Gambia", "gn": "Guinea",
    "gp": "Guadeloupe", "gq": "Equatorial Guinea", "gr": "Greece", "gt": "Guatemala",
    "gu": "Guam", "gw": "Guinea-Bissau", "gy": "Guyana", "hk": "Hong Kong",
    "hm": "Heard Island and McDonald Islands", "hn": "Honduras", "hr": "Croatia",
    "ht": "Haiti", "hu": "Hungary", "id": "Indonesia", "ie": "Ireland", "il": "Israel",
    "im": "Isle of Man", "in": "India", "io": "British Indian Ocean Territory", "iq": "Iraq",
    "ir": "Iran", "is": "Iceland", "it": "Italy", "je": "Jersey", "jm": "Jamaica",
    "jn": "Jinmen", "jo": "Jordan", "jp": "Japan", "ke": "Kenya", "kg": "Kyrgyzstan",
    "kh": "Cambodia", "ki": "Kiribati", "km": "Comoros", "kn": "Saint Kitts and Nevis",
    "kp": "North Korea", "kr": "South Korea", "kw": "Kuwait", "ky": "Cayman Islands",
    "kz": "Kazakhstan", "la": "Lao People's Democratic Republic", "lb": "Lebanon",
    "lc": "Saint Lucia", "li": "Liechtenstein", "lk": "Sri Lanka", "lr": "Liberia",
    "ls": "Lesotho", "lt": "Lithuania", "lu": "Luxembourg", "lv": "Latvia", "ly": "Libya",
    "ma": "Morocco", "mc": "Monaco", "md": "Moldova", "me": "Montenegro",
    "mf": "Saint Martin", "mg": "Madagascar", "mh": "Marshall Islands", "mk": "North Macedonia",
    "ml": "Mali", "mm": "Myanmar", "mn": "Mongolia", "mo": "Macao", "mp": "Northern Mariana Islands",
    "mq": "Martinique", "mr": "Mauritania", "ms": "Montserrat", "mt": "Malta", "mu": "Mauritius",
    "mv": "Maldives", "mw": "Malawi", "mx": "Mexico", "my": "Malaysia", "mz": "Mozambique",
    "na": "Namibia", "nc": "New Caledonia", "ne": "Niger", "nf": "Norfolk Island",
    "ng": "Nigeria", "ni": "Nicaragua", "nl": "Netherlands", "no": "Norway", "np": "Nepal",
    "nr": "Nauru", "nu": "Niue", "nz": "New Zealand", "om": "Oman", "pa": "Panama",
    "pe": "Peru", "pf": "French Polynesia", "pg": "Papua New Guinea", "ph": "Philippines",
    "pk": "Pakistan", "pl": "Poland", "pm": "Saint Pierre and Miquelon", "pn": "Pitcairn",
    "pr": "Puerto Rico", "pt": "Portugal", "pw": "Palau", "py": "Paraguay", "qa": "Qatar",
    "re": "Réunion", "ro": "Romania", "rs": "Serbia", "ru": "Russia", "rw": "Rwanda",
    "sa": "Saudi Arabia", "sb": "Solomon Islands", "sc": "Seychelles", "sd": "Sudan",
    "se": "Sweden", "sg": "Singapore", "sh": "Saint Helena", "si": "Slovenia",
    "sj": "Svalbard and Jan Mayen", "sk": "Slovakia", "sl": "Sierra Leone", "sm": "San Marino",
    "sn": "Senegal", "so": "Somalia", "sr": "Suriname", "ss": "South Sudan",
    "st": "São Tomé and Príncipe", "sv": "El Salvador", "sx": "Sint Maarten",
    "sy": "Syria", "sz": "Eswatini", "tc": "Turks and Caicos Islands", "td": "Chad",
    "tf": "French Southern Territories", "tg": "Togo", "th": "Thailand", "tj": "Tajikistan",
    "tk": "Tokelau", "tl": "Timor-Leste", "tm": "Turkmenistan", "tn": "Tunisia",
    "to": "Tonga", "tr": "Turkey", "tt": "Trinidad and Tobago", "tv": "Tuvalu",
    "tz": "Tanzania", "ua": "Ukraine", "ug": "Uganda", "um": "United States Minor Outlying Islands",
    "us": "United States", "uy": "Uruguay", "uz": "Uzbekistan", "va": "Vatican City",
    "vc": "Saint Vincent and the Grenadines", "ve": "Venezuela", "vg": "British Virgin Islands",
    "vi": "U.S. Virgin Islands", "vn": "Vietnam", "vu": "Vanuatu", "wf": "Wallis and Futuna",
    "ws": "Samoa", "xk": "Kosovo", "ye": "Yemen", "yt": "Mayotte", "za": "South Africa",
    "zm": "Zambia", "zw": "Zimbabwe"
}

def generate_fake_passport(country_code="us"):
    fake = Faker()
    return {
        "Name": fake.name(),
        "Gender": fake.random_element(elements=('Male', 'Female')),
        "Street Address": fake.street_address(),
        "City": fake.city(),
        "State": fake.state(),
        "Pincode": fake.postcode(),
        "Country": COUNTRY_CODES.get(country_code, "Unknown Country"),
        "Mobile Number": fake.phone_number(),
        "Email": fake.email(),
        "IBAN": fake.iban(),
        "Driver's License Number": fake.license_plate(),
        "Social Security Number": fake.ssn()
    }

def format_passport_details(passport_details):
    country = passport_details.get("Country", "Unknown Country")
    response = [
        f"**{country} Address Generated** ✅",
        "", 
        "▰▰▰▰▰▰▰▰▰▰▰▰▰"
    ]
    for key, value in passport_details.items():
        response.append(f"•➥ **{key}**: `{value}`")
    return "\n".join(response)


@app.on_message(filters.command(["fake"], prefixes=[".", "/"]))
async def send_fake_passport_details(client, message):
    command_text = message.text.split()
    country_code = command_text[1] if len(command_text) > 1 and command_text[1] in COUNTRY_CODES else "us"
    passport_details = generate_fake_passport(country_code)
    formatted_details = format_passport_details(passport_details)
    await client.send_message(message.chat.id, formatted_details)
