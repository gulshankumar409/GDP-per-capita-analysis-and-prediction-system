from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,PasswordField,IntegerField
from wtforms.validators import ValidationError,DataRequired,Email,EqualTo

class Predict(FlaskForm):
    Population=StringField("Enter Population of Country",validators=[DataRequired()])
    Area = StringField("Enter Area (sq. km) ", validators=[DataRequired()])
    Coastline  = StringField("Enter Coastline (coast/area ratio)", validators=[DataRequired()])
    Net_migration = StringField("Enter Net migration", validators=[DataRequired()])
    Infant_mortality = StringField("Enter Infant mortality (per 1000 births)", validators=[DataRequired()])
    Litracy  = StringField("Enter Literacy (%)  ", validators=[DataRequired()])
    Phones = StringField("Enter Phones (per 1000) ", validators=[DataRequired()])
    Crops  = StringField("Enter Crops (%)", validators=[DataRequired()])
    Other = StringField("Enter Other (%other than crops)", validators=[DataRequired()])
    Birthrate  = StringField("Enter Birthrate ", validators=[DataRequired()])
    Agriculture  = StringField("Enter Agriculture rate", validators=[DataRequired()])
    Country=SelectField("Country",
                        choices=[(0,'Afghanistan'), (1,'Albania'), (2,'Algeria'), (3,'American Samoa'), (4,'Andorra'),
                                 (5, 'Angola'), (6,'Anguilla'), (7,'Antigua & Barbuda'), (8,'Argentina'), (9,'Armenia'),
                                 (10,'Aruba'), (11,'Australia'), (12, 'Austria' ), (13, 'Azerbaijan'), (14, 'Bahamas, The'),
                                 (15, 'Bahrain' ), (16, 'Bangladesh'), (17,'Barbados'), (18, 'Belarus'), (19,'Belgium'),
                                 (20, 'Belize'), (21, 'Benin'), ( 22, 'Bermuda'), (23, 'Bhutan'), (24, 'Bolivia'),
                                 (25, 'Bosnia & Herzegovina' ), (26, 'Botswana'), (27, 'Brazil'), (28,'British Virgin Is.'),
                                 (29,'Brunei'), (30,'Bulgaria'), (31,'Burkina Faso'), (32, 'Burma'), (33, 'Burundi'),
                                 (34,'Cambodia'), (35, 'Cameroon' ), (36,'Canada'), (37, 'Cape Verde' ), (38, 'Cayman Islands'),
                                 (39,'Central African Rep.' ), (40,'Chad'), (41, 'Chile' ), (42, 'China'), (43, 'Colombia' ),
                                 (44, 'Comoros'), (45,'Congo, Dem. Rep.'), (46,'Congo, Repub. of the' ), (47,'Cook Islands'),
                                 (48,'Costa Rica'), (49,"Cote d'Ivoire"), (50,'Croatia'), (51,'Cuba'), (52,'Cyprus'),
                                 (53,'Czech Republic'), (54,'Denmark'), (55,'Djibouti'), (56,'Dominica'),
                                 (57,'Dominican Republic'), (58,'East Timor'), (59, 'Ecuador'), (60, 'Egypt' ),
                                 (61, 'El Salvador'), (62,'Equatorial Guinea'), (63,'Eritrea'), (64,'Estonia'),
                                 (65,'Ethiopia'), (66,'Faroe Islands'), (67, 'Fiji'), (68, 'Finland'), (69,'France'),
                                 (70,'French Guiana'), (71,'French Polynesia'), (72,'Gabon'), (73,'Gambia, The'),
                                 (74, 'Gaza Strip'), (75,'Georgia'), (76, 'Germany'), (77,'Ghana'), (78,'Gibraltar'),
                                 (79,'Greece'), (80,'Greenland'), (81,'Grenada'), (82,'Guadeloupe'), (83,'Guam'),
                                 (84,'Guatemala'), (85,'Guernsey'), (86,'Guinea'), (87,'Guinea-Bissau'), (88,'Guyana'),
                                 (89,'Haiti'), (90,'Honduras'), (91,'Hong Kong'), (92,'Hungary'), (93,'Iceland'),
                                 (94,'India'), (95,'Indonesia'), (96,'Iran'), (97,'Iraq'), (98, 'Ireland'),
                                 (99, 'Isle of Man'), (100,'Israel'), (101,'Italy'), (102,'Jamaica'), (103,'Japan'),
                                 (104,'Jersey'), (105,'Jordan'), (106, 'Kazakhstan'), (107,'Kenya'), (108,'Kiribati'),
                                 (109, 'Korea, North'), (110, 'Korea, South'), (111,'Kuwait'), (112, 'Kyrgyzstan'),
                                 (113,'Laos'), (114,'Latvia'), (115,'Lebanon'), (116,'Lesotho'), (117,'Liberia'),
                                 (118,'Libya'), (119,'Liechtenstein'), (120,'Lithuania' ), (121,'Luxembourg'), (122,'Macau'),
                                 (123,'Macedonia'), (124,'Madagascar'), (125,'Malawi'), (126,'Malaysia'), (127,'Maldives'),
                                 (128,'Mali'), (129,'Malta'), (130,'Marshall Islands'), (131,'Martinique'),
                                 (132,'Mauritania'), (133,'Mauritius'), (134,'Mayotte'), (135, 'Mexico'),
                                 (136,'Micronesia, Fed. St.'), (137,'Moldova'), (138,'Monaco'), (139,'Mongolia'),
                                 (140,'Montserrat'), (141,'Morocco'), (142,'Mozambique'), (143,'Namibia'), (144,'Nauru'),
                                 (145,'Nepal'), (146,'Netherlands'), (147,'Netherlands Antilles'), (148,'New Caledonia'),
                                 (149,'New Zealand'), (150,'Nicaragua'), (151,'Niger'), (152,'Nigeria'),
                                 (153,'N. Mariana Islands'), (154,'Norway'), (155,'Oman'), (156,'Pakistan'), (157,'Palau'),
                                 (158,'Panama' ), (159,'Papua New Guinea'), (160,'Paraguay'), (161,'Peru'),
                                 (162,'Philippines'), (163,'Poland'), (164,'Portugal'), (165,'Puerto Rico'), (166,'Qatar'),
                                 (167,'Reunion'), (168,'Romania'), (169,'Russia'), (170,'Rwanda'), (171,'Saint Helena'),
                                 (172,'Saint Kitts & Nevis'), (173,'Saint Lucia'), (174,'St Pierre & Miquelon'),
                                 (175,'Saint Vincent and the Grenadines'), (176,'Samoa'), (177,'San Marino'),
                                 (178,'Sao Tome & Principe'), (179,'Saudi Arabia'), (180,'Senegal'), (181,'Serbia'),
                                 (182,'Seychelles'), (183,'Sierra Leone'), (184,'Singapore'), (185,'Slovakia'),
                                 (186,'Slovenia'), (187,'Solomon Islands'), (188,'Somalia'), (189,'South Africa'),
                                 (190,'Spain'), (191,'Sri Lanka'), (192,'Sudan'), (193,'Suriname'), (194,'Swaziland'),
                                 (195,'Sweden'), (196,'Switzerland'), (197,'Syria'), (198,'Taiwan'), (199,'Tajikistan'),
                                 (200,'Tanzania'), (201,'Thailand'), (202,'Togo'), (203,'Tonga'), (204,'Trinidad & Tobago'),
                                 (205,'Tunisia'), (206,'Turkey'), (207,'Turkmenistan'), (208,'Turks & Caicos Is'),
                                 (209,'Tuvalu'), (210,'Uganda'), (211,'Ukraine'), (212,'United Arab Emirates'),
                                 (213,'United Kingdom'), (214,'United States'), (215,'Uruguay'), (216,'Uzbekistan'),
                                 (217,'Vanuatu'), (218,'Venezuela'), (219,'Vietnam'), (220,'Virgin Islands'),
                                 (221,'Wallis and Futuna'), (222,'West Bank'), (223,'Western Sahara'), (224,'Yemen'),
                                 (225,'Zambia'), (226,'Zimbabwe')])
    Region = SelectField('Region',
                           choices=[('Region_ASIA (EX. NEAR EAST)', 'Region_ASIA (EX. NEAR EAST)'), ('Region_BALTICS', 'Region_BALTICS'),
                                    ('Region_C.W. OF IND. STATES', 'Region_C.W. OF IND. STATES'), ('Region_EASTERN EUROPE', 'Region_EASTERN EUROPE'),
                                    ('Region_LATIN AMER. & CARIB ', 'Region_LATIN AMER. & CARIB '), ('Region_NEAR EAST)', 'Region_NEAR EAST'),
                                    ('Region_NORTHERN AFRICA ', 'Region_NORTHERN AFRICA '), ('Region_NORTHERN AMERICA', 'Region_NORTHERN AMERICA'),
                                    ('Region_OCEANIA', 'Region_OCEANIA'), ('Region_SUB-SAHARAN AFRICA ', 'Region_SUB-SAHARAN AFRICA '),
                                    ('Region_WESTERN EUROPE', 'Region_WESTERN EUROPE')])

    submit=SubmitField("Predict")
