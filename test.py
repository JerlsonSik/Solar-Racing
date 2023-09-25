import math

def cartesian_to_azimuth(x, y, z):
    # Calculate azimuth angle
    azimuth = math.atan2(y, x)  # atan2(y, x) returns angle in radians
    azimuth_deg = math.degrees(azimuth)  # Convert radians to degrees
    if azimuth_deg < 0:
        azimuth_deg += 360  # Ensure angle is in the range [0, 360)
    return azimuth_deg

# Example coordinates
x = -0.195
y = 0.23902
z = 0.1101

azimuth_angle = cartesian_to_azimuth(x, y, z)
print(f"Azimuth angle: {azimuth_angle} degrees")