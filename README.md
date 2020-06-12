# Final Project Graphics
**Stage 1: Work**
*Features Implemented*
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
  * Adding Multiple Light Sources
      * MDL file syntax for light: light name r b g x y z
      * If you define a light with the same name twice, the later light definition will replace the original
      * The first light is always called "firstLight"
  * Changing Behavior of Vary
      * Using vary to move lights
      * New function: move_light
          * MDL syntax: move_light [name] x y z [knob]
          * move_light name x y z
              * Moves the specified light x units in the x-axis, y units in the y-axis, and z units in the z-axis
          * move_light x y z
              * Moves all lights x units in the x-axis, y units in the y-axis, and z units in the z-axis
              
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

Thursday, 6/11/2020
* Rachel:
  * Finished implementing more light sources
  * Made cactus for gif
  * Worked with Kayla to finish move_light

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
  * Adding Multiple Light Sources
      * MDL file syntax for light: light name r b g x y z
      * If you define a light with the same name twice, the later light definition will replace the original
      * The first light is always called "firstLight"
  * Changing Behavior of Vary
    * Adding a parameter to calculate change over time using functions including:
      * Linear, Quadratic, Cubic, etc.
      * Sine/Cosine Function
      * Arbitrary
    * Using vary to move lights
      * New function: move_light
      * MDL syntax: move_light [name] x y z [knob]
        * move_light name x y z
            * Moves the specified light x units in the x-axis, y units in the y-axis, and z units in the z-axis
        * move_light x y z
            * Moves all lights x units in the x-axis, y units in the y-axis, and z units in the z-axis
