Rails.application.routes.draw do
  get  'backtests/:yr', to: 'backtests#index'
  get  'posts/index'
  root 'posts#index'
  get  ':controller(/:action)'
  # get ':controller(/:action(/:id(.:format)))'
  get 'about'     => 'posts#about'
  get 'blog'      => 'posts#blog'
  get 'contact'   => 'posts#contact'
  get 'backtests' => 'backtests#index'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
