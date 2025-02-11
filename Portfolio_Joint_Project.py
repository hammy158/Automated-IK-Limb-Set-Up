import maya.cmds as cmds
'''This script makes an IK leg joint chain, makes it functional with an IKH and a controller.'''

selected_limb = ''

def execute_functions():
    if selected_limb:
        create_joint_chain()
        apply_ikh()
        create_controller()
    
#Create a function that makes a 3 joint, joint chain
def create_joint_chain():
    global selected_limb
    if selected_limb == 'leg':
        cmds.select(clear=True)  # Clear selection before creating joints

        # Create leg joints
        thigh = cmds.joint(n='thighIK_JNT', p=(0, 4, 0))
        knee = cmds.joint(n='kneeIK_JNT', p=(0, 2, 1))
        ankle = cmds.joint(n='ankleIK_JNT', p=(0, 0, 0))
        
        # Orient the joints correctly
        cmds.joint(thigh, e=True, zso=True, oj='xyz')
        cmds.joint(knee, e=True, zso=True, oj='xyz')
    elif selected_limb == 'arm':
        cmds.select(clear=True)  # Clear selection before creating joints

        # Create arm joints
        shoulder = cmds.joint(n='shoulderIK_JNT', p=(0, 4, 0))
        elbow = cmds.joint(n='elbowIK_JNT', p=(0, 2, -1))
        wrist = cmds.joint(n='wristIK_JNT', p=(0, 0, 0))
        
        # Orient the joints correctly
        cmds.joint(shoulder, e=True, zso=True, oj='xyz')
        cmds.joint(elbow, e=True, zso=True, oj='xyz')
    
#Create a function that applies a rp ikh to the joint chain
def apply_ikh():
    global selected_limb
    if selected_limb == 'leg':
        cmds.ikHandle(n= 'leg_IKH', sj='thighIK_JNT', ee='ankleIK_JNT')
    elif selected_limb == 'arm':
        cmds.ikHandle(n= 'arm_IKH', sj='shoulderIK_JNT', ee='wristIK_JNT')
        
#Create a function that creates a controller that controls the IKH
def create_controller():
    global selected_limb
    if selected_limb == 'leg':
        cmds.circle( n= 'legIK_CTRL', nr=(0, 1, 0), c=(0, 0, 0) )
        cmds.parent('leg_IKH', 'legIK_CTRL')
    elif selected_limb == 'arm':
        cmds.circle( n= 'armIK_CTRL', nr=(0, 1, 0), c=(0, 0, 0) )
        cmds.parent('arm_IKH', 'armIK_CTRL')
#The way to choose the limbs
def create_window():
    def limb_arm(args):
        global selected_limb
        selected_limb = 'arm'
        close_window()
        execute_functions()
    def limb_leg(args):
        global selected_limb
        selected_limb = 'leg'
        close_window()
        execute_functions()
    cmds.window(t = 'Limb Selection', width=250 )
    cmds.columnLayout( adjustableColumn=True )
    cmds.button( label='Arm', command=limb_arm )
    cmds.button( label='Leg', command=limb_leg )
    cmds.showWindow()
def close_window():
    """Closes the window after a selection is made."""
    if cmds.window('limbWindow', exists=True):
        cmds.deleteUI('limbWindow', window=True)


create_window()
