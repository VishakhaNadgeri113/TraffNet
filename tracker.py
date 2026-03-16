import math

class Tracker:
    def __init__(self):
        self.center_points = {}
        self.id_count = 0

    def update(self, objects_rect):
        objects_bbs_ids = []

        for rect in objects_rect:
            x,y,x1,y1 = rect
            cx = (x+x1)//2
            cy = (y+y1)//2

            same_object_detected = False
            for id,pt in self.center_points.items():
                dist = math.hypot(cx-pt[0],cy-pt[1])

                if dist < 35:
                    self.center_points[id] = (cx,cy)
                    objects_bbs_ids.append([x,y,x1,y1,id])
                    same_object_detected = True
                    break

            if not same_object_detected:
                self.center_points[self.id_count] = (cx,cy)
                objects_bbs_ids.append([x,y,x1,y1,self.id_count])
                self.id_count += 1

        return objects_bbs_ids
