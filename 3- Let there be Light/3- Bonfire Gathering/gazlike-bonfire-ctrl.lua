
--[[
		This constant is to check whether is close enough to react to it. Remember that
		the proximity sensor readings decrease with the distance of the sense obstacle.
  ]]
DELTA = 0.001


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
	-- We treat each proximity reading as a vector whose length is given by the value
	-- and whose angle is given by the angle corresponding to the reading
	-- First, we sum all these vectors into a variable called 'accum'
		accum = { x=0, y=0 }
   		for i = 1,24 do
		-- This is the way to initialize a vector from length and angle
    		local vec = {
				x = robot.proximity[i].value * math.cos(robot.proximity[i].angle),
				y = robot.proximity[i].value * math.sin(robot.proximity[i].angle)
			}
		-- Sum the 'vec' to the accumulator 'accum'
    		accum.x = accum.x + vec.x
    		accum.y = accum.y + vec.y
		end
	-- Now 'accum' is a vector that points to the direction of the closest obstacle
	-- OK, this is not always true. In fact, if two obstacles are located at symmetric
	-- positions around a robot, 'accum' will be zero. However, in practice these
	-- cases don't really count. Try it yourself to see that it's true!
	-- Get the angle of the accumulator
		angle = math.atan2(accum.y, accum.x)
	-- Get the length of the accumulator / 24 (in this way, we are sure that it is
	-- between 0 and 1 and setting a good value for delta is easy)
		length = math.sqrt(accum.x*accum.x + accum.y*accum.y) / 24
	-- Is the closest obstacle very close?
   		if (length < DELTA) then
		-- No obstacle, keep going straight
      		robot.wheels.set_velocity(50,50)
		else
			--if there is any blob nearby then bonfire is near, do a full stop
			if #robot.colored_blob_omnidirectional_camera>0 then
                robot.wheels.set_velocity(0, 0)
            else	
		-- bounce away depending on the direction of the obstacle
      			if angle > 0 then
			-- The obstacle is on the left, turn to the right
         			robot.wheels.set_velocity(25,-10)
      			else
			-- The obstacle is on the right, turn to the left
         			robot.wheels.set_velocity(-10,25)
      			end
			end
		end
	end
	POS = robot.positioning.position
	log(robot.id..' '..POS.x.." "..POS.y)
end

--[[ Controller reset ]]
function reset()
	-- nothing to do
end

--[[ Controller destroy ]]
function destroy()
	-- nothing to do
end
