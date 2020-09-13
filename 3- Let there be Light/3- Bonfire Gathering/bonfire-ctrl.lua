
-- The base wheel speed
SPEED = 20


--[[ Controller init ]]
function init()
    robot.colored_blob_omnidirectional_camera.enable()
    if robot.id =="fb0" then
        robot.leds.set_all_colors("red")
    end
end

--[[ Controller step ]]
function step()
    if robot.id ~= "fb0" then
        value = -1 -- highest value found so far
	    idx = -1   -- index of the highest value
            
        for i=1,24 do
		    if value < robot.proximity[i].value then
			    idx = i
			    value = robot.proximity[i].value
		    end
	    end
	-- At this point, 'value' contains the highest proximity reading found
 	-- and 'idx' contains the index of that sensor
	    if value == 0 then
		-- The robot has no obstacles around, just go straight
		    robot.wheels.set_velocity(SPEED, SPEED)
	    else
        -- The robot has obstacles, set wheels according to 'idx'
        --if there is a blob nearby it mean the robot is near the beacon, do full stop
            if #robot.colored_blob_omnidirectional_camera>0 then
                robot.wheels.set_velocity(0, 0)
            else
		        if idx <= 12 then
			-- The closest obstacle is between 0 and 180 degrees: soft turn towards the right
			        robot.wheels.set_velocity(SPEED, (idx-1) * SPEED / 11)
		        else
			-- The closest obstacle is between 180 and 360 degrees: soft turn towards the left
			        robot.wheels.set_velocity((24-idx) * SPEED / 11, SPEED)
		        end
	        end
        end
        
    end
end

--[[ Controller reset ]]
function reset()
	init()
end

--[[ Controller destroy ]]
function destroy()
	-- nothing to do
end