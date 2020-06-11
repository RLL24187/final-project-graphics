# Final Project Graphics

**Stage 0: Proposal**

*Group Members:*
* Kayla Fang (Period 10)
* Rachel Leong (Period 10)

*List of Features We Want to Implement:*
* Existing MDL Commands/Features to Implement
  * light
* Modified Existing MDL Commands/Features to Implement
  * Adding New Primitive Shapes:
    * Wedge
      * Starting Point: left-bottom-front vertex (x, y, z)
      * add_wedge( polygons, x, y, z, width, height, depth )
    * Square pyramid
      * Starting Point: top vertex (x, y, z)
      * add_pyramid( polygons, x, y, z, width, height, depth )
    * Cylinder
      * Starting Point: center of bottom of cylinder (cx, cy, cz)
      * Generates an upright standing cylinder with center aligning with the y-axis
      * add_cylinder(polygons, cx, cy, cz, radius, height, step)
    * Cone:
      * Starting Point: center of bottom of cone (cx, cy, cz)
      * Generates an upright standing cone with center aligning with the y-axis
      * add_cone(polygons, cx, cy, cz, radius, height, step)
  * Adding More Light Sources
  * Changing Behavior of Vary
    * Adding a parameter to calculate change over time using functions including:
      * Linear, Quadratic, Cubic, etc.
      * Sine/Cosine Function
      * Arbitrary
    * Using vary to move lights
      * Include a parameter to specify a light source to vary

**Stage 1: Work**

*Development Log*

Thursday, 5/28/2020
* Kayla:
  * Wrote the code for add_wedge and add_pyramid
* Rachel:
  * Wrote the code for generate_cylinder and add_cylinder, but doesn't quite work yet

Friday, 5/29/2020
* Rachel:
  * Finished generate_cylinder and add_cylinder
  * Finished generate_cone and add_cone

Wednesday, 6/3/2020
* Rachel & Kayla:
  * Discussed how to use vary to move lights

Thursday, 6/4/2020
* Rachel & Kayla:
  * Started to write the code for how to move the light source

Wednesday, 6/10/2020
* Kayla:
  * Worked on testing the moving light --> the middle images are not displaying correctly
