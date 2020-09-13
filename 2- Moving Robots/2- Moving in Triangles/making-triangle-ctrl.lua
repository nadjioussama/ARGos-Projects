
function init()
    --start the step counter
    counter=1

end

function step()
    --after 10 step make a turn left
    if (counter % 10 ~= 0) then
        robot.wheels.set_velocity(30,30)--robot moving in a straight line
    else 
        robot.wheels.set_velocity(0,300)--the robot making a 60° turn
    end

    counter = counter + 1 
end

function reset()
    log("new cycle")
end

function destroy()
    log("goodbye")
end

