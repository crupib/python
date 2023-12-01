box = Rectangle()
box.width = 100.0
box.height = 200.0 
box.corner = Point() 
box.corner.x = 0.0 
box.corner.y = 0.0
center = find_center(box)
print_point(center)
box.width = box.width + 50
box.height = box.height + 100
grow_rectangle(box,50,100)
box.width, box.height
box2 = copy.copy(box)
box2 is box
box2.corner is box.corner
