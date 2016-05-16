require 'test_helper'

class BacktestsControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get backtests_index_url
    assert_response :success
  end

  test "should get btyr" do
    get backtests_btyr_url
    assert_response :success
  end

end
