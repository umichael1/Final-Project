# test_project.py
# Unit tests for project.py functions using pytest.
# AI assistance was used to refine test cases.

import project
import pytest
import random

def test_update_trex():
    """Test the T-Rex's jump mechanics."""
    # Reset state
    state = {'trex_y': 0, 'jumping': False, 'velocity': 0}
    project.state.update(state)
    
    # Test no movement when not jumping
    project.update_trex(0.1)
    assert project.state['trex_y'] == 0
    
    # Test jump initiation
    project.start_jump()
    project.update_trex(0.1)
    expected_y = 0 + project.JUMP_VELOCITY * 0.1 - 0.5 * project.GRAVITY * 0.1**2
    assert project.state['trex_y'] == pytest.approx(expected_y, abs=1e-5)
    
    # Test landing
    while project.state['jumping']:
        project.update_trex(0.1)
    assert project.state['trex_y'] == 0
    assert not project.state['jumping']

def test_update_obstacles():
    """Test obstacle movement and generation."""
    # Reset state with controlled randomness
    random.seed(42)
    state = {
        'obstacles': [100, 200],
        'total_time': 0,
        'next_obstacle_time': 1.0
    }
    project.state.update(state)
    
    # Test obstacle movement
    project.update_obstacles(0.1)
    assert project.state['obstacles'] == [100 - project.SPEED * 0.1, 200 - project.SPEED * 0.1]
    
    # Test obstacle removal
    project.state['obstacles'] = [-project.CACTUS_WIDTH - 1, 50]
    project.update_obstacles(0.1)
    assert project.state['obstacles'] == [50 - project.SPEED * 0.1]
    
    # Test obstacle generation
    project.state['total_time'] = 1.0
    initial_len = len(project.state['obstacles'])
    project.update_obstacles(0.1)
    assert len(project.state['obstacles']) > initial_len

def test_detect_collision():
    """Test collision detection between T-Rex and obstacles."""
    # Reset state
    state = {'trex_y': 0, 'obstacles': [10]}
    project.state.update(state)
    
    # Test collision when overlapping
    assert project.detect_collision() == True
    
    # Test no collision when T-Rex is above obstacle
    project.state['trex_y'] = project.CACTUS_HEIGHT + 1
    assert project.detect_collision() == False
    
    # Test no collision when obstacle is out of range
    project.state['obstacles'] = [project.TREX_WIDTH + 1]
    project.state['trex_y'] = 0
    assert project.detect_collision() == False