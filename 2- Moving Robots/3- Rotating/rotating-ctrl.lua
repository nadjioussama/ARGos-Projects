
function init()
    --start the step counter
    counter=1

end

function step()
    --after 5 step make rotate to the left with approximaly Pi/3 angle
    if (counter % 5 == 0) then
        robot.wheels.set_velocity(-60,60)--every 5 step, robot make 60° turn to the left on its axis
    else
        robot.wheels.set_velocity(0,0)--otherwise robot stays still
    end

    counter = counter + 1 
end

function reset()
    log("new cycle")
end

function destroy()
    log("goodbye")
end

