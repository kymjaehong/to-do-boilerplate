package com.example.todo.ui

import android.os.Bundle
import android.view.View
import androidx.fragment.app.viewModels
import com.example.todo.databinding.FragmentNavigationExampleBinding
import com.example.todo.ui.viewmodel.NavigationExampleViewModel
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class NavigationExampleFragment: BaseFragment<FragmentNavigationExampleBinding>() {

    override fun getViewBinding(): FragmentNavigationExampleBinding {
        return FragmentNavigationExampleBinding.inflate(layoutInflater)
    }

    private val viewModel by viewModels<NavigationExampleViewModel>()

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {}
}