function MoveAndTurn(forwardSpeed, angulerSpeed)
    leftSpeed = forwardSpeed - angulerSpeed
    righSpeed = forwardSpeed + angulerSpeed
    
    robot.wheels.set_velocity(leftSpeed, righSpeed)
end

function init()
    --start the step counter
    counter=1
end

function step()
    --after 10 step make a turn left
    if (counter % 10 ~= 0) then
        MoveAndTurn(30,0)-- the robot is moving in a straight line
    else 
        MoveAndTurn(0,300)--after 10 steps the robot make a 60° turn to the left
    end

    counter = counter + 1 
end

function reset()
    log("new cycle")
end

function destroy()
    log("goodbye")
end

