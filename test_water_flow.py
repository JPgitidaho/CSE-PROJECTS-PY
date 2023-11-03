
from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height,\
pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number,\
pressure_loss_from_pipe_reduction, kPa_to_psi, calculate_filling_time


def test_water_column_height():
    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == 7.5
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == 57.9
    
    
def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx(0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs=0.001)



def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0,abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008,abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462,abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)


def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0, 3)    == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)


def test_reynolds_number():
    assert abs(reynolds_number(0.048692, 0) - 0) < 1
    assert abs(reynolds_number(0.048692, 1.65) - 80069) < 1
    assert abs(reynolds_number(0.048692, 1.75) - 84922) < 1
    assert abs(reynolds_number(0.28687, 1.65) - 471729) < 1
    assert abs(reynolds_number(0.28687, 1.75) - 500318) < 1


def test_pressure_loss_from_pipe_reduction():
    assert abs(pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692) - 0) < 0.001
    assert abs(pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) + 163.744) < 0.001
    assert abs(pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) + 184.182) < 0.001


def test_kPa_to_psi_conversion():
    # Test case 1
    kPa = 0
    expected_psi = 0
    actual_psi = kPa_to_psi(kPa)
    assert actual_psi == approx(expected_psi, abs=0.001)

   # Test case 2
    kPa = 50
    expected_psi = 7.2519
    actual_psi = kPa_to_psi(kPa)
    assert actual_psi == approx(expected_psi, abs=0.001)

    # Test case 3
    kPa = 150
    expected_psi = 21.7557
    actual_psi = kPa_to_psi(kPa)
    assert actual_psi == approx(expected_psi, abs=0.001)
    
    # Test case 4
    kPa = 300
    expected_psi = 43.5114
    actual_psi = kPa_to_psi(kPa)
    assert actual_psi == approx(expected_psi, abs=0.001)

    # Test case 5
    kPa = 500
    expected_psi = 72.519
    actual_psi = kPa_to_psi(kPa)
    assert actual_psi == approx(expected_psi, abs=0.001)

    # Test case 6
    kPa = 600
    expected_psi = 87.0228
    actual_psi = kPa_to_psi(kPa)
    assert actual_psi == approx(expected_psi, abs=0.001)
    

def test_calculate_filling_time():
    # Test case 1
    flow_rate = 0.5  # cubic meters per second
    tank_volume = 8  # cubic meters
    expected_time = 16.0  # seconds
    assert calculate_filling_time(flow_rate, tank_volume) == approx(expected_time, rel=1e-2)


    # Test case 2
    flow_rate = 0.75  # cubic meters per second
    tank_volume = 5  # cubic meters
    expected_time = 6.67  # seconds
    assert calculate_filling_time(flow_rate, tank_volume) == approx(expected_time, rel=1e-2)

    # Test case 3
    flow_rate = 1.5  # cubic meters per second
    tank_volume = 20  # cubic meters
    expected_time = 13.33  # seconds
    assert calculate_filling_time(flow_rate, tank_volume) == approx(expected_time, rel=1e-2)




# Call the main function that is part of pytest so that the computer will execute
#the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

