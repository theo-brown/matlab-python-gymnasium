classdef MountainCar < handle
    properties
			state
			action_range
			position_range
			max_speed
			cpower
    end
    
    methods
        function obj = MountainCar(action_range, position_range, max_speed, cpower)
			obj.action_range = action_range;
            obj.position_range = position_range;
            obj.max_speed = max_speed;
            obj.cpower = cpower;
        end

        function state = reset(obj)
            obj.state = [0, 0];
            state = obj.state;
        end
        
        function state = step(obj, action)
			position = obj.state(1);
			velocity = obj.state(2);
			force = min(max(action, obj.action_range(1)), obj.action_range(2));
			velocity = velocity + force * obj.cpower - 0.0025 * cos(position * 3);
			if velocity > obj.max_speed
					velocity = obj.max_speed;
			end
			if velocity < -obj.max_speed
					velocity = -obj.max_speed;
			end
			position = position + velocity;
			if position > obj.position_range(2)
					position = obj.position_range(2);
			end
			if position < obj.position_range(1)
					position = obj.position_range(1);
			end
			if position == obj.position_range(1) && velocity < 0
					velocity = 0;
			end
			obj.state = [position, velocity];
			state = obj.state;
        end
    end
end
