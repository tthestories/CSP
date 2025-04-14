import csv
import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Climate Data Explorer")

# Load temperature anomaly data
temp_data = []
with open('GlobalTempAnomaly.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        temp_data.append({'year': int(row[0]), 'anomaly': float(row[1])})

# Process data for visualization
min_anomaly = min([d['anomaly'] for d in temp_data])
max_anomaly = max([d['anomaly'] for d in temp_data])
avg_anomaly = sum([d['anomaly'] for d in temp_data]) / len(temp_data)
min_year = [d['year'] for d in temp_data if d['anomaly'] == min_anomaly][0]
max_year = [d['year'] for d in temp_data if d['anomaly'] == max_anomaly][0]

# Visualization loop (simplified)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    # Draw temperature anomaly graph (line graph logic here)
    pygame.display.flip()

pygame.quit()
