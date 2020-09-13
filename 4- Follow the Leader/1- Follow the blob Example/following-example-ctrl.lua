function init()
	robot.colored_blob_omnidirectional_camera.enable()
	if robot.id == "fb1" then
		robot.leds.set_single_color(13,"red")
	end
	
end

function moving(distance, angle)

	--as we noticed in the making squares project, at angular velocity =110 we get 90° turn, we used it to get other angles but deviding by 90
	if angle ~=0 then --the target is not at 0° of the robot, so adjust the robot accordingly
		ratio = angle/90
		forwardSpeed = distance * ratio
		angularSpeed = 110 * ratio
		leftV = forwardSpeed - angularSpeed
		rightV = forwardSpeed + angularSpeed
		
		robot.wheels.set_velocity(leftV,rightV)
	else
		--the target is directly in line of sight, move forward until distance is 30
		if distance == 30 then
			robot.wheels.set_velocity(0,0)
		else
			robot.wheels.set_velocity(20,20)
		end
	end
end

function step()
	if robot.id =="fb2" then
		blob = robot.colored_blob_omnidirectional_camera[1] --get the blob object
		distance = math.floor(blob.distance) --get a rounded value of the distance
		angle = math.floor(math.deg(blob.angle)) --get the angle of the blob in degree mode
		log("distance : "..distance.."cm")
		log("angle : "..angle.."°")
		log(robot.id.." is moving toward the light..")
		if distance < 2 then 
			moving(0,0)
		else
			moving(distance,angle) --make the robot move to that angle with that distance
		end
	end

end


function reset()

end


function destroy()

end