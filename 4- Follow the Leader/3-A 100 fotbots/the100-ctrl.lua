DELTA = 0.001
function init()--the same algorithm from the last project, we only added two more robots with leds
	robot.colored_blob_omnidirectional_camera.enable()
    if robot.id =="fb0" or robot.id=="fb13" or robot.id =="fb20" or robot.id =="fb25" then
        robot.leds.set_all_colors("red")
    end
end


function moving(distance, angle)
	if angle ~=0 then
		ratio = angle/90
		forwardSpeed = distance * ratio
		angularSpeed = 110 * ratio
		leftV = forwardSpeed - angularSpeed
		rightV = forwardSpeed + angularSpeed
		
		robot.wheels.set_velocity(leftV,rightV)
	else
		if (distance<20) then
			robot.wheels.set_velocity(0,0)
		else
			robot.wheels.set_velocity(75,75)
		end
	end
end

function step()
		accum = { x=0, y=0 }
   		for i = 1,24 do
    		local vec = {
				x = robot.proximity[i].value * math.cos(robot.proximity[i].angle),
				y = robot.proximity[i].value * math.sin(robot.proximity[i].angle)
			}
    		accum.x = accum.x + vec.x
    		accum.y = accum.y + vec.y
		end
		angle = math.atan2(accum.y, accum.x)
		length = math.sqrt(accum.x*accum.x + accum.y*accum.y) / 24
		if (length < DELTA) then
	  		robot.wheels.set_velocity(150,150)
		else

			if #robot.colored_blob_omnidirectional_camera>0 then
                blob = robot.colored_blob_omnidirectional_camera[1]
				distance = math.floor(blob.distance)
				lightAngle = math.floor(math.deg(blob.angle))
				if robot.id~= "fb0" or robot.id~="fb13" or robot.id~="fb20" or robot.id~="fb25" then
					moving(distance,lightAngle)
				end
            else	
	  			if angle > 0 then
	     			robot.wheels.set_velocity(25,-10)
      			else
	     			robot.wheels.set_velocity(-10,25)
      			end
			end
		end
	
end


function reset()
	init()
end


function destroy()
end
