import pandas as pd

# Load the CSV file
df = pd.read_csv('stored_light.csv')

# Print the columns to debug
print("Columns in the DataFrame:", df.columns.tolist())

# Open the KML file for writing
with open('output.kml', 'w', encoding='utf-8') as kml_file:
    # Write the KML header
    kml_file.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
    kml_file.write('''<kml xmlns="http://www.opengis.net/kml/2.2">\n''')
    kml_file.write('  <Document>\n')
    kml_file.write('    <name>lights4ΤΕΣΤ</name>\n')
    kml_file.write('    <open>1</open>\n')
    kml_file.write('    <Style id="defaultStyle">\n')
    kml_file.write('      <BalloonStyle>\n')
    kml_file.write('        <text><![CDATA[$[description]]]></text>\n')
    kml_file.write('      </BalloonStyle>\n')
    kml_file.write('    </Style>\n')

    # Write folder details
    kml_file.write('    <Folder>\n')
    kml_file.write('      <name>Λίστα Φωτιστικών</name>\n')
    kml_file.write('      <visibility>1</visibility>\n')

    # Loop through each row in the dataframe
    for index, row in df.iterrows():
        try:
            # Ensure latitude and longitude are valid
            lat = float(row['Latitude'].replace(',', '.'))
            lon = float(row['Longitude'].replace(',', '.'))
        except ValueError as e:
            print(f"Error converting row {index + 2}: {e}")
            continue
        
        # Write placemark details
        kml_file.write('      <Placemark>\n')
        kml_file.write(f'        <name>Row: {index + 2}</name>\n')
        kml_file.write(f'        <LookAt>\n')
        kml_file.write(f'          <longitude>{lon:.6f}</longitude>\n')
        kml_file.write(f'          <latitude>{lat:.6f}</latitude>\n')
        kml_file.write('          <range>1000</range>\n')
        kml_file.write('        </LookAt>\n')
        kml_file.write('        <Point>\n')
        kml_file.write(f'          <coordinates>{lon:.6f},{lat:.6f},0</coordinates>\n')
        kml_file.write('        </Point>\n')
        
        # Manually add the CDATA section with table content
        kml_file.write('        <description><![CDATA[\n')
        kml_file.write('          <style type="text/css">*{font-family:Verdana,Arial,Helvetica,Sans-Serif;}</style>\n')
        kml_file.write('          <table>\n')
        kml_file.write(f'            <tr><td><b>α/α</b></td><td>{index + 1}</td></tr>\n')
        kml_file.write(f'            <tr><td><b>Δημ.Διαμ</b></td><td>{row.get("Δημ.Διαμ", "")}</td></tr>\n')
        kml_file.write(f'            <tr><td><b>Οδός</b></td><td>{row.get("Οδός", "")}</td></tr>\n')
        kml_file.write(f'            <tr><td><b>Pillar ID Number</b></td><td>{row.get("Pillar ID Number", "")}</td></tr>\n')
        kml_file.write(f'            <tr><td><b>Light ID Number</b></td><td>{row.get("Light ID Number", "")}</td></tr>\n')
        kml_file.write(f'            <tr><td><b>Latitude</b></td><td>{lat:.6f}</td></tr>\n')
        kml_file.write(f'            <tr><td><b>Longitude</b></td><td>{lon:.6f}</td></tr>\n')
        kml_file.write(f'            <tr><td><b>Τύπος Κολώνας</b></td><td>{row.get("Τύπος Κολώνας", "")}</td></tr>\n')
        kml_file.write(f'            <tr><td><b>Τύπος Φωτιστικού Α</b></td><td>{row.get("Τύπος Φωτιστικού Α", "")}</td></tr>\n')
        kml_file.write(f'            <tr><td><b>Google Maps Link</b></td><td><a href="http://maps.google.com/maps?q=loc:{lat},{lon}">Google Maps Link</a></td></tr>\n')
        kml_file.write('          </table>\n')
        kml_file.write('        ]]></description>\n')

        kml_file.write('      </Placemark>\n')

    # Close the folder and document tags
    kml_file.write('    </Folder>\n')
    kml_file.write('  </Document>\n')
    kml_file.write('</kml>\n')

print("KML file created successfully!")
