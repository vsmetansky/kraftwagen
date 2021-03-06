from datetime import date

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from showroom.utils import CHAR_FIELD_DEFAULT_SIZE_M, CHAR_FIELD_DEFAULT_SIZE_L, CHAR_FIELD_DEFAULT_SIZE_S


class Fullname(models.Model):
    first_name = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M)
    second_name = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M, blank=True, null=True)
    surname = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M)

    def __str__(self):
        return ' '.join((self.first_name, self.surname))


class Position(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M, unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(1)
    ])
    responsibilities = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M)
    requirements = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M)

    def __str__(self):
        return self.name


class Employee(models.Model):
    SEXES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)

    age = models.IntegerField(default=18, validators=[
        MinValueValidator(18)
    ])
    sex = models.CharField(max_length=1, choices=SEXES)
    address = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M)
    passport = models.IntegerField(unique=True, validators=[
        MaxValueValidator(1000000000000),
        MinValueValidator(0)
    ])

    def __str__(self):
        return f'{self.fullname}, {self.position}'


class Manufacturer(models.Model):
    COUNTRIES = (('AW', 'Aruba'), ('AF', 'Afghanistan'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AX', 'Åland Islands'),
                 ('AL', 'Albania'), ('AD', 'Andorra'), ('AE', 'United Arab Emirates'), ('AR', 'Argentina'),
                 ('AM', 'Armenia'), ('AS', 'American Samoa'), ('AQ', 'Antarctica'),
                 ('TF', 'French Southern Territories'), ('AG', 'Antigua and Barbuda'), ('AU', 'Australia'),
                 ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BI', 'Burundi'), ('BE', 'Belgium'), ('BJ', 'Benin'),
                 ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BF', 'Burkina Faso'), ('BD', 'Bangladesh'),
                 ('BG', 'Bulgaria'), ('BH', 'Bahrain'), ('BS', 'Bahamas'), ('BA', 'Bosnia and Herzegovina'),
                 ('BL', 'Saint Barthélemy'), ('BY', 'Belarus'), ('BZ', 'Belize'), ('BM', 'Bermuda'),
                 ('BO', 'Bolivia, Plurinational State of'), ('BR', 'Brazil'), ('BB', 'Barbados'),
                 ('BN', 'Brunei Darussalam'), ('BT', 'Bhutan'), ('BV', 'Bouvet Island'), ('BW', 'Botswana'),
                 ('CF', 'Central African Republic'), ('CA', 'Canada'), ('CC', 'Cocos (Keeling) Islands'),
                 ('CH', 'Switzerland'), ('CL', 'Chile'), ('CN', 'China'), ('CI', "Côte d'Ivoire"), ('CM', 'Cameroon'),
                 ('CD', 'Congo, The Democratic Republic of the'), ('CG', 'Congo'), ('CK', 'Cook Islands'),
                 ('CO', 'Colombia'), ('KM', 'Comoros'), ('CV', 'Cabo Verde'), ('CR', 'Costa Rica'), ('CU', 'Cuba'),
                 ('CW', 'Curaçao'), ('CX', 'Christmas Island'), ('KY', 'Cayman Islands'), ('CY', 'Cyprus'),
                 ('CZ', 'Czechia'), ('DE', 'Germany'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DK', 'Denmark'),
                 ('DO', 'Dominican Republic'), ('DZ', 'Algeria'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('ER', 'Eritrea'),
                 ('EH', 'Western Sahara'), ('ES', 'Spain'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FI', 'Finland'),
                 ('FJ', 'Fiji'), ('FK', 'Falkland Islands (Malvinas)'), ('FR', 'France'), ('FO', 'Faroe Islands'),
                 ('FM', 'Micronesia, Federated States of'), ('GA', 'Gabon'), ('GB', 'United Kingdom'),
                 ('GE', 'Georgia'), ('GG', 'Guernsey'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GN', 'Guinea'),
                 ('GP', 'Guadeloupe'), ('GM', 'Gambia'), ('GW', 'Guinea-Bissau'), ('GQ', 'Equatorial Guinea'),
                 ('GR', 'Greece'), ('GD', 'Grenada'), ('GL', 'Greenland'), ('GT', 'Guatemala'), ('GF', 'French Guiana'),
                 ('GU', 'Guam'), ('GY', 'Guyana'), ('HK', 'Hong Kong'), ('HM', 'Heard Island and McDonald Islands'),
                 ('HN', 'Honduras'), ('HR', 'Croatia'), ('HT', 'Haiti'), ('HU', 'Hungary'), ('ID', 'Indonesia'),
                 ('IM', 'Isle of Man'), ('IN', 'India'), ('IO', 'British Indian Ocean Territory'), ('IE', 'Ireland'),
                 ('IR', 'Iran, Islamic Republic of'), ('IQ', 'Iraq'), ('IS', 'Iceland'), ('IL', 'Israel'),
                 ('IT', 'Italy'), ('JM', 'Jamaica'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('JP', 'Japan'),
                 ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KG', 'Kyrgyzstan'), ('KH', 'Cambodia'), ('KI', 'Kiribati'),
                 ('KN', 'Saint Kitts and Nevis'), ('KR', 'Korea, Republic of'), ('KW', 'Kuwait'),
                 ('LA', "Lao People's Democratic Republic"), ('LB', 'Lebanon'), ('LR', 'Liberia'), ('LY', 'Libya'),
                 ('LC', 'Saint Lucia'), ('LI', 'Liechtenstein'), ('LK', 'Sri Lanka'), ('LS', 'Lesotho'),
                 ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LV', 'Latvia'), ('MO', 'Macao'),
                 ('MF', 'Saint Martin (French part)'), ('MA', 'Morocco'), ('MC', 'Monaco'),
                 ('MD', 'Moldova, Republic of'), ('MG', 'Madagascar'), ('MV', 'Maldives'), ('MX', 'Mexico'),
                 ('MH', 'Marshall Islands'), ('MK', 'North Macedonia'), ('ML', 'Mali'), ('MT', 'Malta'),
                 ('MM', 'Myanmar'), ('ME', 'Montenegro'), ('MN', 'Mongolia'), ('MP', 'Northern Mariana Islands'),
                 ('MZ', 'Mozambique'), ('MR', 'Mauritania'), ('MS', 'Montserrat'), ('MQ', 'Martinique'),
                 ('MU', 'Mauritius'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('YT', 'Mayotte'), ('NA', 'Namibia'),
                 ('NC', 'New Caledonia'), ('NE', 'Niger'), ('NF', 'Norfolk Island'), ('NG', 'Nigeria'),
                 ('NI', 'Nicaragua'), ('NU', 'Niue'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('NP', 'Nepal'),
                 ('NR', 'Nauru'), ('NZ', 'New Zealand'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PA', 'Panama'),
                 ('PN', 'Pitcairn'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PW', 'Palau'), ('PG', 'Papua New Guinea'),
                 ('PL', 'Poland'), ('PR', 'Puerto Rico'), ('KP', "Korea, Democratic People's Republic of"),
                 ('PT', 'Portugal'), ('PY', 'Paraguay'), ('PS', 'Palestine, State of'), ('PF', 'French Polynesia'),
                 ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'),
                 ('SA', 'Saudi Arabia'), ('SD', 'Sudan'), ('SN', 'Senegal'), ('SG', 'Singapore'),
                 ('GS', 'South Georgia and the South Sandwich Islands'),
                 ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJ', 'Svalbard and Jan Mayen'),
                 ('SB', 'Solomon Islands'), ('SL', 'Sierra Leone'), ('SV', 'El Salvador'), ('SM', 'San Marino'),
                 ('SO', 'Somalia'), ('PM', 'Saint Pierre and Miquelon'), ('RS', 'Serbia'), ('SS', 'South Sudan'),
                 ('ST', 'Sao Tome and Principe'), ('SR', 'Suriname'), ('SK', 'Slovakia'), ('SI', 'Slovenia'),
                 ('SE', 'Sweden'), ('SZ', 'Eswatini'), ('SX', 'Sint Maarten (Dutch part)'), ('SC', 'Seychelles'),
                 ('SY', 'Syrian Arab Republic'), ('TC', 'Turks and Caicos Islands'), ('TD', 'Chad'), ('TG', 'Togo'),
                 ('TH', 'Thailand'), ('TJ', 'Tajikistan'), ('TK', 'Tokelau'), ('TM', 'Turkmenistan'),
                 ('TL', 'Timor-Leste'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'),
                 ('TR', 'Turkey'), ('TV', 'Tuvalu'), ('TW', 'Taiwan, Province of China'),
                 ('TZ', 'Tanzania, United Republic of'), ('UG', 'Uganda'), ('UA', 'Ukraine'),
                 ('UM', 'United States Minor Outlying Islands'), ('UY', 'Uruguay'), ('US', 'United States'),
                 ('UZ', 'Uzbekistan'), ('VA', 'Holy See (Vatican City State)'),
                 ('VC', 'Saint Vincent and the Grenadines'), ('VE', 'Venezuela, Bolivarian Republic of'),
                 ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('VN', 'Viet Nam'),
                 ('VU', 'Vanuatu'), ('WF', 'Wallis and Futuna'), ('WS', 'Samoa'), ('YE', 'Yemen'),
                 ('ZA', 'South Africa'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe'))

    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)

    name = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M, unique=True)
    address = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M)
    country = models.CharField(max_length=2, choices=COUNTRIES)

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M, unique=True)
    specifications = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_L)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(1)
    ])

    def __str__(self):
        return self.name


class BodyType(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M, unique=True)
    description = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_L)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)
    facility_1 = models.ForeignKey(
        Facility, related_name='car_facility_1', on_delete=models.SET_NULL, blank=True, null=True)
    facility_2 = models.ForeignKey(
        Facility, related_name='car_facility_2', on_delete=models.SET_NULL, blank=True, null=True)
    facility_3 = models.ForeignKey(
        Facility, related_name='car_facility_3', on_delete=models.SET_NULL, blank=True, null=True)

    brand = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M)
    date_produced = models.DateField(default=date.today)
    color = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_S)
    body_number = models.IntegerField(unique=True, validators=[
        MinValueValidator(0)
    ])
    engine_number = models.IntegerField(unique=True, validators=[
        MinValueValidator(0)
    ])
    specifications = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_L)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(1)
    ])

    def __str__(self):
        return f'{self.manufacturer}, {self.brand}, {self.color}'


class Order(models.Model):
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)

    address = models.CharField(max_length=CHAR_FIELD_DEFAULT_SIZE_M, blank=True, null=True)
    phone = models.IntegerField(models.IntegerField(validators=[
        MaxValueValidator(1000000000000),
        MinValueValidator(0)
    ]))
    passport = models.IntegerField(validators=[
        MaxValueValidator(1000000000000),
        MinValueValidator(0)
    ])
    date_ordered = models.DateField(default=date.today)
    date_sold = models.DateField(default=date.today)
    is_processed = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    prepay_percent = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return f'{self.fullname}: {self.car}'
