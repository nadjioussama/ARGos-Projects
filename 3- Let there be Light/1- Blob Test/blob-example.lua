
function init()
    robot.colored_blob_omnidirectional_camera.enable()
    if (robot.id =="fb1") then
        robot.leds.set_single_color(13,"red")
    else
        robot.leds.set_single_color(13,"green")
    end
end

function step()
    for i = 1, #robot.colored_blob_omnidirectional_camera do
        blob = robot.colored_blob_omnidirectional_camera[i]
        log(robot.id.." : (r, g, b) = ("..blob.color.red..", "..blob.color.green..", "..blob.color.blue..")")
        log(robot.id.." : Angle = "..blob.angle)
        log(robot.id.." : Distance = "..blob.distance)
    end
end

function reset()
   
end

function destroy()
  
end

