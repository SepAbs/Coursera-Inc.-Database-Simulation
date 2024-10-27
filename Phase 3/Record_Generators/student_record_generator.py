from faker import Faker
import random

faker = Faker()

num_records = 2000

# Define possible values for educational_level
educational_levels = ['Bachelors', 'Master', 'Phd']


universities = [
    "Harvard University",
    "Stanford University",
    "Massachusetts Institute of Technology (MIT)",
    "University of Oxford",
    "California Institute of Technology (Caltech)",
    "University of Cambridge",
    "Princeton University",
    "University of Chicago",
    "Yale University",
    "Columbia University",
    "University of Pennsylvania",
    "University of California, Berkeley",
    "University of California, Los Angeles (UCLA)",
    "University of Michigan",
    "Cornell University",
    "Duke University",
    "Johns Hopkins University",
    "Northwestern University",
    "University of Toronto",
    "Imperial College London",
    "London School of Economics and Political Science (LSE)",
    "University College London (UCL)",
    "New York University",
    "University of Edinburgh",
    "University of California, San Diego",
    "University of California, San Francisco",
    "University of Hong Kong",
    "University of Melbourne",
    "University of Sydney",
    "Australian National University",
    "National University of Singapore",
    "King's College London",
    "McGill University",
    "University of British Columbia",
    "University of Tokyo",
    "Tsinghua University",
    "Peking University",
    "Seoul National University",
    "University of Queensland",
    "Monash University",
    "University of New South Wales",
    "University of Amsterdam",
    "University of Copenhagen",
    "ETH Zurich",
    "Ecole Polytechnique Fédérale de Lausanne",
    "Karolinska Institute",
    "University of Manchester",
    "University of Bristol",
    "University of Warwick",
    "University of Glasgow",
    "Durham University",
    "Lund University",
    "University of Helsinki",
    "University of Oslo",
    "University of Auckland",
    "University of Cape Town",
    "University of São Paulo",
    "Purdue University",
    "University of Wisconsin-Madison",
    "University of Illinois at Urbana-Champaign",
    "Ohio State University",
    "University of Minnesota",
    "University of Texas at Austin",
    "University of Washington",
    "University of North Carolina at Chapel Hill",
    "Boston University",
    "Pennsylvania State University",
    "University of Southern California",
    "Michigan State University",
    "University of Maryland, College Park",
    "Rutgers University",
    "University of Pittsburgh",
    "University of Florida",
    "Texas A&M University",
    "University of Arizona",
    "Indiana University Bloomington",
    "University of Virginia",
    "Georgia Institute of Technology",
    "University of Miami",
    "Vanderbilt University",
    "Washington University in St. Louis",
    "Emory University",
    "University of Notre Dame",
    "University of Rochester",
    "Tufts University",
    "Brandeis University",
    "Case Western Reserve University",
    "Rice University",
    "Dartmouth College",
    "University of Iowa",
    "University of Colorado Boulder",
    "University of Oregon",
    "University of Utah",
    "University of Missouri",
    "University of Nebraska-Lincoln",
    "University of South Carolina",
    "University of Alabama",
    "University of Tennessee",
    "University of Kentucky",
    "University of Kansas",
    "University of Oklahoma",
    "Oklahoma State University",
    "University of Mississippi",
    "University of Arkansas",
    "Louisiana State University",
    "University of Georgia",
    "Florida State University",
    "University of South Florida",
    "University of Central Florida",
    "Virginia Tech",
    "George Mason University",
    "University of Connecticut",
    "Rutgers University–Newark",
    "University of Delaware",
    "University at Buffalo, SUNY",
    "Stony Brook University, SUNY",
    "University of Vermont",
    "University of New Hampshire",
    "University of Rhode Island",
    "University of Maine",
    "University of Massachusetts Amherst",
    "University of Massachusetts Boston",
    "University of Massachusetts Lowell",
    "University of Massachusetts Dartmouth",
    "University of Alaska Fairbanks",
    "University of Hawaii at Manoa",
    "University of Montana",
    "Montana State University",
    "University of Wyoming",
    "University of Idaho",
    "University of Nevada, Reno",
    "University of Nevada, Las Vegas",
    "University of New Mexico",
    "New Mexico State University",
    "Arizona State University",
    "Northern Arizona University",
    "University of Colorado Denver",
    "Colorado State University",
    "University of Denver",
    "University of North Dakota",
    "North Dakota State University",
    "South Dakota State University",
    "University of South Dakota",
    "University of Nebraska at Omaha",
    "Creighton University",
    "Wichita State University",
    "Kansas State University",
    "Missouri State University",
    "University of Missouri–Kansas City",
    "University of Missouri–St. Louis",
    "University of Iowa",
    "Iowa State University",
    "University of Northern Iowa",
    "University of Minnesota Duluth",
    "University of Minnesota Twin Cities",
    "Michigan Technological University",
    "Central Michigan University",
    "Western Michigan University",
    "Eastern Michigan University",
    "Northern Michigan University",
    "University of Michigan-Flint",
    "University of Michigan-Dearborn",
    "Wayne State University",
    "Oakland University",
    "Saginaw Valley State University",
    "Ferris State University",
    "Grand Valley State University",
    "Ball State University",
    "Indiana University – Purdue University Indianapolis",
    "Purdue University Fort Wayne",
    "Indiana State University",
    "University of Southern Indiana",
    "Southern Illinois University Carbondale",
    "Southern Illinois University Edwardsville",
    "University of Illinois at Chicago",
    "University of Illinois Springfield",
    "Northern Illinois University",
    "Western Illinois University",
    "Eastern Illinois University",
    "Illinois State University",
    "University of Wisconsin-Milwaukee",
    "University of Wisconsin-Eau Claire",
    "University of Wisconsin-La Crosse",
    "University of Wisconsin-Oshkosh",
    "University of Wisconsin-Parkside",
    "University of Wisconsin-Platteville",
    "University of Wisconsin-River Falls",
    "University of Wisconsin-Stevens Point",
    "University of Wisconsin-Stout",
    "University of Wisconsin-Whitewater",
    "University of Wisconsin-Green Bay",
    "University of Wisconsin-Superior",
    "Kent State University",
    "University of Akron",
    "Bowling Green State University",
    "Miami University",
    "Ohio University",
    "University of Cincinnati",
    "Cleveland State University",
    "Wright State University",
    "University of Toledo",
    "Youngstown State University",
    "University of Dayton",
    "Xavier University",
    "University of Kentucky",
    "University of Louisville",
    "Western Kentucky University",
    "Eastern Kentucky University",
    "Murray State University",
    "Morehead State University",
    "Northern Kentucky University",
    "Auburn University",
    "University of Alabama",
    "University of Alabama at Birmingham",
    "University of Alabama in Huntsville",
    "Alabama A&M University",
    "Alabama State University",
    "University of South Alabama",
    "Troy University",
    "Jacksonville State University",
    "University of North Alabama",
    "Samford University",
    "University of West Alabama",
    "Mississippi State University",
    "University of Mississippi",
    "University of Southern Mississippi",
    "Jackson State University",
    "Mississippi University for Women",
    "Alcorn State University",
    "Mississippi Valley State University",
    "Delta State University",
    "University of Arkansas",
    "University of Arkansas at Little Rock",
    "University of Arkansas at Pine Bluff",
    "Arkansas State University",
    "University of Central Arkansas",
    "Arkansas Tech University",
    "Henderson State University",
    "Southern Arkansas University",
    "University of Tennessee",
    "University of Memphis",
    "Middle Tennessee State University",
    "East Tennessee State University",
    "Tennessee State University",
    "Austin Peay State University",
    "University of Tennessee at Chattanooga",
    "University of Tennessee at Martin",
    "Tennessee Technological University",
    "Vanderbilt University",
    "Clemson University",
    "University of South Carolina",
    "Coastal Carolina University",
    "Winthrop University",
    "South Carolina State University",
    "The Citadel, The Military College of South Carolina",
    "University of North Carolina at Chapel Hill",
    "North Carolina State University",
    "Duke University",
    "University of North Carolina at Charlotte",
    "University of North Carolina at Greensboro",
    "East Carolina University",
    "Appalachian State University",
    "Western Carolina University",
    "University of North Carolina at Wilmington",
    "North Carolina Central University",
    "North Carolina A&T State University",
    "Wake Forest University",
    "Florida State University",
    "University of Florida",
    "University of Central Florida",
    "Florida International University",
    "University of South Florida",
    "Florida Atlantic University",
    "University of North Florida",
    "Florida A&M University",
    "Florida Gulf Coast University",
    "University of West Florida",
    "Florida Polytechnic University",
    "Miami University",
    "University of Miami",
    "University of Georgia",
    "Georgia Institute of Technology",
    "Georgia State University",
    "University of Georgia",
    "Kennesaw State University",
    "Georgia Southern University",
    "Valdosta State University",
    "Augusta University",
    "University of West Georgia",
    "Georgia College & State University",
    "University of Kentucky",
    "University of Louisville",
    "Western Kentucky University",
    "Eastern Kentucky University",
    "Murray State University",
    "Morehead State University",
    "Northern Kentucky University",
    "University of Tennessee",
    "University of Memphis",
    "Middle Tennessee State University",
    "East Tennessee State University",
    "Tennessee State University",
    "Austin Peay State University",
    "University of Tennessee at Chattanooga",
    "University of Tennessee at Martin",
    "Tennessee Technological University",
    "Vanderbilt University",
    "University of Alabama",
    "University of Alabama at Birmingham",
    "University of Alabama in Huntsville",
    "Auburn University",
    "Alabama A&M University",
    "Alabama State University",
    "University of South Alabama",
    "Troy University",
    "Jacksonville State University",
    "University of North Alabama",
    "Samford University",
    "University of West Alabama",
    "Mississippi State University",
    "University of Mississippi",
    "University of Southern Mississippi",
    "Jackson State University",
    "Mississippi University for Women",
    "Alcorn State University",
    "Mississippi Valley State University",
    "Delta State University",
    "University of Arkansas",
    "University of Arkansas at Little Rock",
    "University of Arkansas at Pine Bluff",
    "Arkansas State University",
    "University of Central Arkansas",
    "Arkansas Tech University",
    "Henderson State University",
    "Southern Arkansas University",
    "Louisiana State University",
    "University of Louisiana at Lafayette",
    "University of Louisiana at Monroe",
    "Louisiana Tech University",
    "Southeastern Louisiana University",
    "Northwestern State University of Louisiana",
    "Nicholls State University",
    "McNeese State University",
    "Grambling State University",
    "Southern University and A&M College",
    "Texas A&M University",
    "University of Texas at Austin",
    "Texas Tech University",
    "University of North Texas",
    "University of Houston",
    "Texas State University",
    "University of Texas at San Antonio",
    "University of Texas at Arlington",
    "University of Texas at El Paso",
    "University of Texas at Dallas",
    "University of Texas Rio Grande Valley",
    "Sam Houston State University",
    "Stephen F. Austin State University",
    "Texas A&M University–Corpus Christi",
    "Texas A&M University–Kingsville",
    "Texas Woman's University",
    "Tarleton State University",
    "Texas Southern University",
    "Prairie View A&M University",
    "West Texas A&M University",
    "Texas A&M University–Commerce",
    "Texas A&M University–Central Texas",
    "Texas A&M University–San Antonio",
    "Texas A&M University–Texarkana",
    "Texas A&M International University",
    "Texas A&M University–Galveston",
    "University of Texas Health Science Center at Houston",
    "University of Texas Health Science Center at San Antonio",
    "University of Texas MD Anderson Cancer Center",
    "University of Texas Health Science Center at Tyler",
    "University of Texas Southwestern Medical Center",
    "University of Texas Medical Branch",
    "University of Texas School of Public Health",
    "University of Texas School of Dentistry at Houston",
    "University of Texas School of Biomedical Informatics at Houston",
    "University of Texas School of Health Professions at Houston",
    "University of Texas Graduate School of Biomedical Sciences at Houston",
    "University of Texas Health Science Center at San Antonio Dental School",
    "University of Texas Health Science Center at San Antonio Graduate School of Biomedical Sciences",
    "University of Texas Health Science Center at San Antonio School of Health Professions",
    "University of Texas Health Science Center at San Antonio School of Medicine",
    "University of Texas Health Science Center at San Antonio School of Nursing",
    "University of Texas MD Anderson Cancer Center UTHealth Graduate School of Biomedical Sciences",
    "University of Texas Medical Branch School of Health Professions",
    "University of Texas Medical Branch School of Medicine",
    "University of Texas Medical Branch School of Nursing",
    "University of Texas Medical Branch Graduate School of Biomedical Sciences",
    "University of Texas Southwestern Medical Center Graduate School of Biomedical Sciences",
    "University of Texas Southwestern Medical Center School of Health Professions",
    "University of Texas Southwestern Medical Center School of Medicine",
    "University of Texas Southwestern Medical Center School of Nursing",
    "University of Texas School of Public Health at Brownsville",
    "University of Texas School of Public Health at Dallas",
    "University of Texas School of Public Health at El Paso",
    "University of Texas School of Public Health at San Antonio",
    "University of Oklahoma",
    "Oklahoma State University",
    "University of Central Oklahoma",
    "Northeastern State University",
    "Southeastern Oklahoma State University",
    "Southwestern Oklahoma State University",
    "East Central University",
    "Northwestern Oklahoma State University",
    "Cameron University",
    "Langston University",
    "Rogers State University",
    "University of Science and Arts of Oklahoma",
    "Oklahoma Panhandle State University",
    "University of Colorado Boulder",
    "Colorado State University",
    "University of Denver",
    "University of Colorado Denver",
    "University of Northern Colorado",
    "Colorado School of Mines",
    "Colorado College",
    "Regis University",
    "University of Colorado Colorado Springs",
    "Fort Lewis College",
    "Metropolitan State University of Denver",
    "Colorado Mesa University",
    "Adams State University",
    "Western State Colorado University",
    "Colorado State University–Pueblo",
    "Colorado State University–Global Campus",
    "University of Wyoming",
    "University of Montana",
    "Montana State University",
    "Montana Tech of the University of Montana",
    "University of Montana Western",
    "Montana State University Billings",
    "Montana State University–Northern",
    "Rocky Mountain College",
    "Carroll College",
    "University of Idaho",
    "Boise State University",
    "Idaho State University",
    "Lewis–Clark State College",
    "Brigham Young University–Idaho",
    "Northwest Nazarene University",
    "College of Idaho",
    "New Mexico State University",
    "University of New Mexico",
    "New Mexico Highlands University",
    "Western New Mexico University",
    "Eastern New Mexico University",
    "New Mexico Institute of Mining and Technology",
    "Northern Arizona University",
    "University of Arizona",
    "Arizona State University",
    "Grand Canyon University",
    "Prescott College",
    "Embry-Riddle Aeronautical University, Prescott",
    "University of Advancing Technology",
    "Thunderbird School of Global Management",
    "Arizona Christian University",
    "University of Nevada, Reno",
    "University of Nevada, Las Vegas",
    "Nevada State College",
    "Sierra Nevada College",
    "University of Utah",
    "Utah State University",
    "Weber State University",
    "Southern Utah University",
    "Utah Valley University",
    "Brigham Young University",
    "Westminster College",
    "Dixie State University",
    "University of Oregon",
    "Oregon State University",
    "Portland State University",
    "University of Portland",
    "Oregon Institute of Technology",
    "Willamette University",
    "Southern Oregon University",
    "Eastern Oregon University",
    "Western Oregon University",
    "Lewis & Clark College",
    "Linfield College",
    "Pacific University",
    "Reed College",
    "George Fox University",
    "Concordia University",
    "University of Washington",
    "Washington State University",
    "University of Puget Sound",
    "Seattle University",
    "Seattle Pacific University",
    "Western Washington University",
    "Eastern Washington University",
    "Central Washington University",
    "Gonzaga University",
    "Whitman College",
    "Walla Walla University",
    "Pacific Lutheran University",
    "Saint Martin's University",
    "The Evergreen State College",
    "University of Alaska Anchorage",
    "University of Alaska Fairbanks",
    "University of Alaska Southeast",
    "Alaska Pacific University",
    "University of Hawaii at Manoa",
    "University of Hawaii at Hilo",
    "University of Hawaii–West Oahu",
    "Hawaii Pacific University",
    "Chaminade University of Honolulu",
    "Brigham Young University–Hawaii",
    "Stanford University",
    "University of California, Berkeley",
    "University of California, Los Angeles",
    "University of California, San Diego",
    "University of California, San Francisco",
    "University of California, Davis",
    "University of California, Santa Barbara",
    "University of California, Irvine",
    "University of California, Riverside",
    "University of California, Santa Cruz",
    "California Institute of Technology",
    "University of Southern California",
    "California State University, Fullerton",
    "San Diego State University",
    "San Jose State University",
    "California State University, Long Beach",
    "California State University, Northridge",
    "California State University, Sacramento",
    "California State University, Los Angeles",
    "California State University, San Bernardino",
    "California State University, Fresno",
    "California State University, East Bay",
    "California State University, Bakersfield",
    "California State University, San Marcos",
    "California State University, Chico",
    "California State University, Stanislaus",
]


# Generate and print the SQL insert statements
student_id = 1
sql_inserts = []
for student_id in range(1, num_records + 1):
    student_id += 1
    educational_level = random.choice(educational_levels)
    university = random.choice(universities)
    major = faker.job()  # Using job title as a proxy for major

    sql_inserts.append(f"INSERT INTO student (student_id, educational, university, major) VALUES ({student_id}, '{educational_level}', '{university}', '{major}');")

# Write the SQL statements to a file
with open('./student_inserts.sql', 'w', encoding='utf-8') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")