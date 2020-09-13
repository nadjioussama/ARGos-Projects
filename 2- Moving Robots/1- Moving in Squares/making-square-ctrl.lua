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
    if (counter % 10 == 0) then
        MoveAndTurn(0,110) --this make the robot make a 90° turn
    else 
    --otherwise move forward at speed 30cm/s at angular velocity 0
        MoveAndTurn(30,0)
    end

    counter = counter + 1 
end

function reset()
    log("new cycle")
end

function destroy()
    log("goodbye")
end

