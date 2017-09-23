// Mars lander simulator
// Version 1.9
// Mechanical simulation functions
// Gabor Csanyi and Andrew Gee, August 2016

// Permission is hereby granted, free of charge, to any person obtaining
// a copy of this software and associated documentation, to make use of it
// for non-commercial purposes, provided that (a) its original authorship
// is acknowledged and (b) no modified versions of the source code are
// published. Restriction (b) is designed to protect the integrity of the
// exercise for future generations of students. The authors would be happy
// to receive any suggested modifications by private correspondence to
// ahg@eng.cam.ac.uk and gc121@eng.cam.ac.uk.

/* lander.cpp written by Karthik Suresh. To analyze trajectory data for autopilot, change file root of output file.
   Load and build using Xcode or Visual Studio. */

#include "lander.h"

void autopilot (void)
  // Autopilot to adjust the engine throttle, parachute and attitude control
{
    double Delta, Kh, Kp, e, altitude, Pout;
    
    /* For Kh = 0.005 and Kp = 1, lander lands in Scenario 1 in 928.4s and in Scenario 5 in 1600.2s.
       For Kh = 0.00868 and Kp = 20, lander lands in Scenario 1 in 577.6s and in Scenario 5 in 493.2s, where fuel is infinite and parachute not deployed.
     
       With finite fuel Kh = 0.018 and Kp = 80 for lander to land successfully in scenario 1 and 5 with autopilot.
       */
    
    Kh = 0.018;
    Kp = 80;
    
    Delta = ((GRAVITY * MARS_MASS) * (UNLOADED_LANDER_MASS + fuel * FUEL_CAPACITY * FUEL_DENSITY))/(MARS_RADIUS * MARS_RADIUS);
    
    Delta = Delta/MAX_THRUST;
    
    if (stabilized_attitude == false) stabilized_attitude = true;
    
    altitude = position.abs() - MARS_RADIUS;
    
    /* if (altitude < 5000 && velocity.abs() < 500) parachute_status = DEPLOYED;  */
    
    e = - (0.5 + Kh * altitude + velocity * position.norm());
    
    Pout = Kp * e;
    
    if (Pout < -Delta)
    {
        throttle = 0;
    }
    else if (Pout >= -Delta && Pout <= 1 - Delta)
    {
        throttle = Pout + Delta;
    }
    else
    {
        throttle = 1;
    }
  
    ofstream fout;
    fout.open("/Users/admin/Dropbox/Cambridge/1A/Computing/MarsLander/landerproject/alt_actual_descent_rate_data_Kh_" + to_string(Kh) +"_scenario_"+to_string(scenario) + ".txt", ofstream::app );
    if (fout)
    { // file opened successfully
        
        fout << altitude << ' ' << velocity * position.norm()  << endl;
        
    }
    else
    { // file did not open successfully
        cout << "Could not open trajectory file for writing" << endl;
    }

   
    
}

void numerical_dynamics (void)
  // This is the function that performs the numerical integration to update the
  // lander's pose. The time step is delta_t (global variable).
{
    
    // Decleration of local variables
    vector3d acceleration, lander_drag, chute_drag, lander_thrust, gravitational_force, new_position;
    static vector3d previous_position;
    double lander_mass;
    
    
  // Here we can apply an autopilot to adjust the thrust, parachute and attitude
  if (autopilot_enabled) autopilot();

  // Here we can apply 3-axis stabilization to ensure the base is always pointing downwards
  if (stabilized_attitude) attitude_stabilization();
    
    
    // Calculating
    lander_mass = FUEL_CAPACITY * fuel * FUEL_DENSITY + UNLOADED_LANDER_MASS;
    
    lander_drag = -0.5 * DRAG_COEF_LANDER * atmospheric_density(position) * M_PI * LANDER_SIZE * LANDER_SIZE * velocity.abs2() * velocity.norm();
    
    chute_drag = -0.5 * DRAG_COEF_CHUTE * atmospheric_density(position) * 5.0 * 2.0 * LANDER_SIZE * 2.0 * LANDER_SIZE * velocity.abs2() * velocity.norm();
    
    lander_thrust = thrust_wrt_world();
    
    gravitational_force = ((-GRAVITY * MARS_MASS * lander_mass)/position.abs2()) * position.norm();
    
    if (parachute_status == NOT_DEPLOYED || parachute_status == LOST)
    {
        acceleration = (lander_drag + lander_thrust + gravitational_force) * (1/lander_mass);
    }
    if (parachute_status == DEPLOYED)
    {
        acceleration = (lander_drag + lander_thrust + gravitational_force + chute_drag) * (1/lander_mass);
    }

    // Vertlet integration to evaluate subsequent positions of Mars Lander.
    if (simulation_time == 0)
    {
        previous_position  = position;
        position = position + delta_t * velocity;
        velocity = velocity + delta_t * acceleration;
    }
    else
    {
        new_position = 2 * position - previous_position + (delta_t * delta_t * acceleration);
        velocity = (1 / delta_t) * (new_position - position);
        previous_position = position;
        position = new_position;
    }
    
    /* Euler Method
    position = position + velocity * delta_t;
    velocity = velocity + acceleration * delta_t;*/
    
}

void initialize_simulation (void)
  // Lander pose initialization - selects one of 10 possible scenarios
{
  // The parameters to set are:
  // position - in Cartesian planetary coordinate system (m)
  // velocity - in Cartesian planetary coordinate system (m/s)
  // orientation - in lander coordinate system (xyz Euler angles, degrees)
  // delta_t - the simulation time step
  // boolean state variables - parachute_status, stabilized_attitude, autopilot_enabled
  // scenario_description - a descriptive string for the help screen

  scenario_description[0] = "circular orbit";
  scenario_description[1] = "descent from 10km";
  scenario_description[2] = "elliptical orbit, thrust changes orbital plane";
  scenario_description[3] = "polar launch at escape velocity (but drag prevents escape)";
  scenario_description[4] = "elliptical orbit that clips the atmosphere and decays";
  scenario_description[5] = "descent from 200km";
  scenario_description[6] = "";
  scenario_description[7] = "";
  scenario_description[8] = "";
  scenario_description[9] = "";

  switch (scenario) {

  case 0:
    // a circular equatorial orbit
    position = vector3d(1.2*MARS_RADIUS, 0.0, 0.0);
    velocity = vector3d(0.0, -3247.087385863725, 0.0);
    orientation = vector3d(0.0, 90.0, 0.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = false;
    autopilot_enabled = false;
    break;

  case 1:
    // a descent from rest at 10km altitude
    position = vector3d(0.0, -(MARS_RADIUS + 10000.0), 0.0);
    velocity = vector3d(0.0, 0.0, 0.0);
    orientation = vector3d(0.0, 0.0, 90.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = true;
    autopilot_enabled = false;
    break;

  case 2:
    // an elliptical polar orbit
    position = vector3d(0.0, 0.0, 1.2*MARS_RADIUS);
    velocity = vector3d(3500.0, 0.0, 0.0);
    orientation = vector3d(0.0, 0.0, 90.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = false;
    autopilot_enabled = false;
    break;

  case 3:
    // polar surface launch at escape velocity (but drag prevents escape)
    position = vector3d(0.0, 0.0, MARS_RADIUS + LANDER_SIZE/2.0);
    velocity = vector3d(0.0, 0.0, 5027.0);
    orientation = vector3d(0.0, 0.0, 0.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = false;
    autopilot_enabled = false;
    break;

  case 4:
    // an elliptical orbit that clips the atmosphere each time round, losing energy
    position = vector3d(0.0, 0.0, MARS_RADIUS + 100000.0);
    velocity = vector3d(4000.0, 0.0, 0.0);
    orientation = vector3d(0.0, 90.0, 0.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = false;
    autopilot_enabled = false;
    break;

  case 5:
    // a descent from rest at the edge of the exosphere
    position = vector3d(0.0, -(MARS_RADIUS + EXOSPHERE), 0.0);
    velocity = vector3d(0.0, 0.0, 0.0);
    orientation = vector3d(0.0, 0.0, 90.0);
    delta_t = 0.1;
    parachute_status = NOT_DEPLOYED;
    stabilized_attitude = true;
    autopilot_enabled = false;
    break;

  case 6:
    break;

  case 7:
    break;

  case 8:
    break;

  case 9:
    break;

  }
}
