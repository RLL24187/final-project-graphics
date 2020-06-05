
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMBIENT BASENAME BOX CAMERA CO COMMENT CONE CONSTANTS CYLINDER DISPLAY DOUBLE FOCAL FRAMES GENERATE_RAYFILES ID INT LIGHT LINE MESH MOVE POP PUSH PYRAMID ROTATE SAVE SAVE_COORDS SAVE_KNOBS SCALE SCREEN SET SET_KNOBS SHADING SHADING_TYPE SPHERE STRING TEXTURE TORUS TWEEN VARY WEB WEDGE XYZinput :\n            | command inputcommand : COMMENTSYMBOL : XYZ\n              | IDTEXT : SYMBOL\n            | STRINGNUMBER : DOUBLEcommand : POP\n                 | PUSHcommand : SCREEN NUMBER NUMBER\n                 | SCREENcommand : SAVE TEXT TEXTcommand : DISPLAYcommand : SPHERE NUMBER NUMBER NUMBER NUMBER\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER\n               | SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : TORUS NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : CONE NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONE NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | CONE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : PYRAMID NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | PYRAMID NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | PYRAMID SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | PYRAMID SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : WEDGE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | WEDGE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | WEDGE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | WEDGE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOLcommand : MOVE NUMBER NUMBER NUMBER SYMBOL\n               | MOVE NUMBER NUMBER NUMBERcommand : SCALE NUMBER NUMBER NUMBER SYMBOL\n                 | SCALE NUMBER NUMBER NUMBERcommand : ROTATE XYZ NUMBER SYMBOL\n                 | ROTATE XYZ NUMBERcommand : FRAMES NUMBERcommand : BASENAME TEXTcommand : VARY SYMBOL NUMBER NUMBER NUMBER NUMBERcommand : SET SYMBOL NUMBER\n               | SET_KNOBS NUMBERcommand : AMBIENT NUMBER NUMBER NUMBERcommand : CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : SHADING SHADING_TYPEcommand : CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : GENERATE_RAYFILEScommand : MESH CO TEXT\n               | MESH SYMBOL CO TEXT\n               | MESH CO TEXT SYMBOL\n               | MESH SYMBOL CO TEXT SYMBOLcommand : SAVE_KNOBS SYMBOLcommand : SAVE_COORDS SYMBOLcommand : TWEEN NUMBER NUMBER SYMBOL SYMBOLcommand : FOCAL NUMBERcommand : WEBcommand : TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,8,30,36,38,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[-1,0,-1,-3,-9,-10,-12,-14,-68,-77,-2,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'COMMENT':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[3,3,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'POP':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[4,4,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'PUSH':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[5,5,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'SCREEN':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[6,6,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'SAVE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[7,7,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'DISPLAY':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[8,8,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'SPHERE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[9,9,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'TORUS':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[10,10,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'BOX':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[11,11,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'CYLINDER':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[12,12,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'CONE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[13,13,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'PYRAMID':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[14,14,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'WEDGE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[15,15,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'LINE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[16,16,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'MOVE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[17,17,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'SCALE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[18,18,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'ROTATE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[19,19,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'FRAMES':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[20,20,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'BASENAME':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[21,21,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'VARY':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[22,22,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'SET':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[23,23,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'SET_KNOBS':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[24,24,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'AMBIENT':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[25,25,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'CONSTANTS':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[26,26,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'LIGHT':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[27,27,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'SHADING':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[28,28,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'CAMERA':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[29,29,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'GENERATE_RAYFILES':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[30,30,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'MESH':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[31,31,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'SAVE_KNOBS':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[32,32,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'SAVE_COORDS':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[33,33,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'TWEEN':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[34,34,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'FOCAL':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[35,35,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'WEB':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[36,36,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'TEXTURE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,65,66,69,73,77,78,80,82,83,102,104,109,129,130,131,133,137,138,141,158,159,164,165,167,168,169,173,175,185,190,191,192,193,195,196,197,198,199,201,203,209,211,212,213,214,215,216,217,218,219,220,221,223,225,227,228,229,230,231,232,235,238,244,245,],[37,37,-3,-9,-10,-12,-14,-68,-77,-8,-6,-7,-4,-5,-57,-58,-61,-66,-73,-74,-76,-11,-13,-56,-60,-69,-52,-54,-55,-62,-71,-70,-15,-51,-53,-72,-75,-17,-16,-19,-27,-31,-59,-18,-20,-21,-23,-28,-29,-32,-33,-35,-39,-43,-67,-22,-24,-25,-30,-34,-36,-37,-40,-41,-44,-45,-47,-65,-26,-38,-42,-46,-49,-48,-50,-63,-64,-78,]),'DOUBLE':([6,9,10,11,12,13,14,15,16,17,18,20,24,25,29,34,35,39,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,67,68,70,71,72,74,79,81,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,105,106,107,108,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,132,134,135,136,140,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,160,161,162,163,166,170,171,172,174,176,177,178,179,180,181,182,183,184,186,187,188,189,194,200,202,204,205,206,207,208,210,222,224,226,233,234,236,237,238,239,240,241,242,243,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-8,-4,-5,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'STRING':([7,21,41,42,43,44,45,75,110,],[43,43,43,-6,-7,-4,-5,43,43,]),'XYZ':([7,9,10,11,12,13,14,15,16,19,21,22,23,26,27,31,32,33,37,40,41,42,43,44,45,75,102,109,110,111,127,129,130,138,139,141,157,168,169,173,175,192,193,196,198,199,201,203,213,217,219,221,223,231,],[44,44,44,44,44,44,44,44,44,64,44,44,44,44,44,44,44,44,44,-8,44,-6,-7,-4,-5,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'ID':([7,9,10,11,12,13,14,15,16,21,22,23,26,27,31,32,33,37,40,41,42,43,44,45,75,102,109,110,111,127,129,130,138,139,141,157,168,169,173,175,192,193,196,198,199,201,203,213,217,219,221,223,231,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-8,45,-6,-7,-4,-5,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'SHADING_TYPE':([28,],[73,]),'CO':([31,44,45,76,],[75,-4,-5,110,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'input':([0,2,],[1,38,]),'command':([0,2,],[2,2,]),'NUMBER':([6,9,10,11,12,13,14,15,16,17,18,20,24,25,29,34,35,39,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,67,68,70,71,72,74,79,81,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,105,106,107,108,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,132,134,135,136,140,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,160,161,162,163,166,170,171,172,174,176,177,178,179,180,181,182,183,184,186,187,188,189,194,200,202,204,205,206,207,208,210,222,224,226,233,234,236,237,238,239,240,241,242,243,],[39,46,48,50,52,54,56,58,60,62,63,65,69,70,74,79,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,132,133,134,135,136,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,157,160,161,162,163,166,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,184,185,186,187,188,189,192,193,194,196,198,199,200,201,202,203,204,205,206,207,208,209,210,213,217,219,221,222,223,224,225,226,231,233,234,236,237,238,239,240,241,242,243,244,245,]),'TEXT':([7,21,41,75,110,],[41,66,83,109,138,]),'SYMBOL':([7,9,10,11,12,13,14,15,16,21,22,23,26,27,31,32,33,37,41,75,102,109,110,111,127,129,130,138,139,141,157,168,169,173,175,192,193,196,198,199,201,203,213,217,219,221,223,231,],[42,47,49,51,53,55,57,59,61,42,67,68,71,72,76,77,78,81,42,42,131,137,42,139,156,158,159,164,165,167,183,190,191,195,197,211,212,214,215,216,218,220,227,228,229,230,232,235,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> input","S'",1,None,None,None),
  ('input -> <empty>','input',0,'p_input','mdl.py',130),
  ('input -> command input','input',2,'p_input','mdl.py',131),
  ('command -> COMMENT','command',1,'p_command_comment','mdl.py',135),
  ('SYMBOL -> XYZ','SYMBOL',1,'p_SYMBOL','mdl.py',139),
  ('SYMBOL -> ID','SYMBOL',1,'p_SYMBOL','mdl.py',140),
  ('TEXT -> SYMBOL','TEXT',1,'p_TEXT','mdl.py',144),
  ('TEXT -> STRING','TEXT',1,'p_TEXT','mdl.py',145),
  ('NUMBER -> DOUBLE','NUMBER',1,'p_NUMBER','mdl.py',149),
  ('command -> POP','command',1,'p_command_stack','mdl.py',153),
  ('command -> PUSH','command',1,'p_command_stack','mdl.py',154),
  ('command -> SCREEN NUMBER NUMBER','command',3,'p_command_screen','mdl.py',158),
  ('command -> SCREEN','command',1,'p_command_screen','mdl.py',159),
  ('command -> SAVE TEXT TEXT','command',3,'p_command_save','mdl.py',166),
  ('command -> DISPLAY','command',1,'p_command_show','mdl.py',170),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER','command',5,'p_command_sphere','mdl.py',174),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_sphere','mdl.py',175),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL','command',6,'p_command_sphere','mdl.py',176),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_sphere','mdl.py',177),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_torus','mdl.py',191),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_torus','mdl.py',192),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_torus','mdl.py',193),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_torus','mdl.py',194),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_box','mdl.py',208),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_box','mdl.py',209),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_box','mdl.py',210),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_box','mdl.py',211),
  ('command -> CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_cylinder','mdl.py',225),
  ('command -> CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_cylinder','mdl.py',226),
  ('command -> CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_cylinder','mdl.py',227),
  ('command -> CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_cylinder','mdl.py',228),
  ('command -> CONE NUMBER NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_cone','mdl.py',242),
  ('command -> CONE NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_cone','mdl.py',243),
  ('command -> CONE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_cone','mdl.py',244),
  ('command -> CONE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_cone','mdl.py',245),
  ('command -> PYRAMID NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_pyramid','mdl.py',259),
  ('command -> PYRAMID NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_pyramid','mdl.py',260),
  ('command -> PYRAMID SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_pyramid','mdl.py',261),
  ('command -> PYRAMID SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_pyramid','mdl.py',262),
  ('command -> WEDGE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_wedge','mdl.py',276),
  ('command -> WEDGE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_wedge','mdl.py',277),
  ('command -> WEDGE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_wedge','mdl.py',278),
  ('command -> WEDGE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_wedge','mdl.py',279),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_line','mdl.py',293),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_line','mdl.py',294),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',295),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',296),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',297),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',298),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',9,'p_command_line','mdl.py',299),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',10,'p_command_line','mdl.py',300),
  ('command -> MOVE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_move','mdl.py',321),
  ('command -> MOVE NUMBER NUMBER NUMBER','command',4,'p_command_move','mdl.py',322),
  ('command -> SCALE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_scale','mdl.py',330),
  ('command -> SCALE NUMBER NUMBER NUMBER','command',4,'p_command_scale','mdl.py',331),
  ('command -> ROTATE XYZ NUMBER SYMBOL','command',4,'p_command_rotate','mdl.py',339),
  ('command -> ROTATE XYZ NUMBER','command',3,'p_command_rotate','mdl.py',340),
  ('command -> FRAMES NUMBER','command',2,'p_command_frames','mdl.py',348),
  ('command -> BASENAME TEXT','command',2,'p_command_basename','mdl.py',353),
  ('command -> VARY SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_vary','mdl.py',358),
  ('command -> SET SYMBOL NUMBER','command',3,'p_command_knobs','mdl.py',364),
  ('command -> SET_KNOBS NUMBER','command',2,'p_command_knobs','mdl.py',365),
  ('command -> AMBIENT NUMBER NUMBER NUMBER','command',4,'p_command_ambient','mdl.py',376),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',11,'p_command_constants','mdl.py',382),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_command_constants','mdl.py',383),
  ('command -> LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_light','mdl.py',389),
  ('command -> SHADING SHADING_TYPE','command',2,'p_command_shading','mdl.py',395),
  ('command -> CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_camera','mdl.py',401),
  ('command -> GENERATE_RAYFILES','command',1,'p_command_generate_rayfiles','mdl.py',406),
  ('command -> MESH CO TEXT','command',3,'p_command_mesh','mdl.py',410),
  ('command -> MESH SYMBOL CO TEXT','command',4,'p_command_mesh','mdl.py',411),
  ('command -> MESH CO TEXT SYMBOL','command',4,'p_command_mesh','mdl.py',412),
  ('command -> MESH SYMBOL CO TEXT SYMBOL','command',5,'p_command_mesh','mdl.py',413),
  ('command -> SAVE_KNOBS SYMBOL','command',2,'p_save_knobs','mdl.py',427),
  ('command -> SAVE_COORDS SYMBOL','command',2,'p_save_coords','mdl.py',433),
  ('command -> TWEEN NUMBER NUMBER SYMBOL SYMBOL','command',5,'p_tween','mdl.py',440),
  ('command -> FOCAL NUMBER','command',2,'p_focal','mdl.py',445),
  ('command -> WEB','command',1,'p_web','mdl.py',449),
  ('command -> TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_texture','mdl.py',453),
]