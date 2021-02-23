import cv2
import numpy as np

def draw_line(image, start, end,
              color=(255,255,255),
              thickness=1,
              line_type=cv2.LINE_AA):
    cv2.line(image, start, end, color, thickness, line_type)

def draw_rectangle(image, top_left, bottom_right,
                   color=(255,255,255),
                   thickness=1,
                   line_type=cv2.LINE_AA):
    cv2.rectangle(image, top_left, bottom_right,
                  color, thickness, line_type)

def draw_circle(image, center, radius,
                color=(255,255,255),
                thickness=1,
                line_type=cv2.LINE_AA):
    cv2.circle(image, center, radius, color, thickness, line_type)

def draw_ellipse(image, center, axes, angle, start_angle, end_angle,
                 color=(255,255,255),
                 thickness=1,
                 line_type=cv2.LINE_AA):
    cv2.ellipse(image, center, axes, angle, start_angle, end_angle,
                color, thickness, line_type)

def draw_polylines(image, points, is_closed=True,
                   color=(255,255,255),
                   thickness=1,
                   line_type=cv2.LINE_AA ):
    cv2.polylines(image, points, is_closed,
                  color, thickness, line_type)

def draw_text(image, text, org,
              font_scale=1,
              color=(255,255,255),
              thickness=1,
              font_face=cv2.FONT_HERSHEY_COMPLEX,
              line_type=cv2.LINE_AA):
    cv2.putText(image, text, org, font_face,
                font_scale, color, thickness, line_type	)
